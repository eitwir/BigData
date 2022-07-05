import re
import csv
import argparse
import collections


def argpars():
    parser = argparse.ArgumentParser()
    parser.add_argument('--N', type=int, help='the number of movies you want to select')
    parser.add_argument('--genres', type=str, help='enter the genres you want to see', default='')
    parser.add_argument('--year_from', type=int,  help='enter the year from', default=1900)
    parser.add_argument('--year_to', type=int,  help='enter the year to', default=2023)
    parser.add_argument('--regexp',  type=str,  help='search movie by matching title',  default='')
    return parser.parse_args()


def open_csv_file(file_path):
    with open(file_path, encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        data = list(reader)
    return data[1:]


def averages():
    total = collections.defaultdict(float)
    count = collections.defaultdict(int)
    for line in open_csv_file('files/ratings.csv'):
        total[line[1]] += float(line[2])
        count[line[1]] += 1
    averages = {id: total[id]/count[id] for id in count}
    return averages


def movies_list(averages):
    result = []
    for movies_id, genre, name, year in filter_list_line(open_csv_file('files/movies.csv')):
        result.append([genre, name, year, check_rating(movies_id, averages)])
    result.sort(key=lambda row: (row[0], -row[3], -row[2], row[1]))
    return result


def filter_by_year(year_from, year_to, string):
    pattern = r'\((\d{4})\)'
    if re.search(pattern, string):
        year = int(re.search(r'\((\d{4})\)', string).group(0)[1:-1])
        if year_from <= year <= year_to:
            return True


def filter_by_regexp(name, string):
    pattern = name
    if re.search(pattern, string):
        return True


def filter_by_genres(genre, arg_genre):
    if arg_genre == '' and genre != '(no genres listed)':
        return True
    elif genre == arg_genre and genre != '(no genres listed)':
        return True


def check_rating(movies_id, rating_dict):
    if movies_id in rating_dict:
        return round(rating_dict[movies_id], 1)
    else:
        return 0.1


def check_by_n(N, genre, count):
    if N is None:
        return True
    else:
        count[genre] += 1
        if count[genre] <= N:
            return True


def filter_list_line(data):
    for movie_id, movie_name, movies_genres in data:
        if filter_by_year(args.year_from, args.year_to, movie_name) and filter_by_regexp(args.regexp, movie_name):
            for arg_genre in args.genres.split('|'):
                for genre in movies_genres.split('|'):
                    if filter_by_genres(genre, arg_genre):
                        name = movie_name[:-7]
                        year = int(re.search(r'\((\d{4})\)', movie_name).group(0)[1:-1])
                        yield movie_id, genre, name, year


def result(data):
    print('genre; name; year; rating')
    count = collections.Counter()
    for genre, name, year, rating in data:
        if check_by_n(args.N, genre, count):
            print('{}; {}; {}; {}'.format(genre, name, year, rating))


if __name__ == "__main__":
    args = argpars()
    averages = averages()
    result_list = movies_list(averages)
    result(result_list)