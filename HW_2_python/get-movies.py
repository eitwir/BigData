import re
import csv
import argparse
from collections import Counter
import collections


def get_argpars():
    parser = argparse.ArgumentParser()
    parser.add_argument('--N', type=int, help='the number of movies you want to select')
    parser.add_argument('--genres', type=str, help='enter the genres you want to see', default='')
    parser.add_argument('--year_from', type=int,  help='enter the year from', default=1900)
    parser.add_argument('--year_to', type=int,  help='enter the year to', default=2023)
    parser.add_argument('--regexp',  type=str,  help='search movie by matching title',  default='')
    return parser.parse_args()


def get_data_from_csv(file_path: str):
    with open(file_path, encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        data = list(reader)
    return data[1:]


def get_the_averages():
    total = collections.defaultdict(float)
    count = collections.defaultdict(int)
    for line in get_data_from_csv('files/ratings.csv'):
        total[line[1]] += float(line[2])
        count[line[1]] += 1
    averages = {id: total[id]/count[id] for id in count}
    return averages


def get_movies_list(averages: dict):
    result = []

    for movies_id, genre, name, year in sorted_list_line(get_data_from_csv('files/movies.csv')):
        result.append([genre, name, year, get_and_check_rating(movies_id, averages)])
    # lambda row: (genre, title, year, rating) —> (genre, -rating, -year, title)
    result.sort(key=lambda row: (row[0], -row[3], -row[2], row[1]))
    return result


def check_year_in_range(year_from, year_to: int, string: str):
    pattern = r'\((\d{4})\)'
    result = True

    if re.search(pattern, string):
        year = int(re.search(r'\((\d{4})\)', string).group(0)[1:-1])
        if year_from <= year <= year_to:
            return result


def check_by_regexp(name, string: str):
    result = True

    pattern = name
    if re.search(pattern, string):
        return result


def search_by_genres(genre, arg_genre: str):
    result = True

    if arg_genre == '' and genre != '(no genres listed)':
        return result
    elif genre == arg_genre and genre != '(no genres listed)':
        return result


def get_and_check_rating(movies_id: int, rating_dict: dict):
    if movies_id in rating_dict:
        return round(rating_dict[movies_id], 1)
    else:
        return 0.1


def check_by_n(N: int, genre: str, count: Counter):
    result = True

    if N is None:
        return result
    else:
        count[genre] += 1
        if count[genre] <= N:
            return result


def sorted_list_line(data: list):
    for movie_id, movie_name, movies_genres in data:
        if check_year_in_range(args.year_from, args.year_to, movie_name) and check_by_regexp(args.regexp, movie_name):
            for arg_genre in args.genres.split('|'):
                for genre in movies_genres.split('|'):
                    if search_by_genres(genre, arg_genre):
                        name = movie_name[:-7]
                        year = int(re.search(r'\((\d{4})\)', movie_name).group(0)[1:-1])
                        yield movie_id, genre, name, year


def show_result(data: list):
    print('genre; name; year; rating')
    count = collections.Counter()
    for genre, name, year, rating in data:
        if check_by_n(args.N, genre, count):
            print(f'{genre}; {name}; {year}; {rating}')


if __name__ == "__main__":
    args = get_argpars()
    averages = get_the_averages()
    result_list = get_movies_list(averages)
    show_result(result_list)
