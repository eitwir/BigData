import sys
import argparse
import re
import csv


def get_argpars():
    parser = argparse.ArgumentParser()
    parser.add_argument('--genres', type=str, help='enter the genres you want to see', default='')
    parser.add_argument('--year_from', type=int, help='enter the year from', default=1900)
    parser.add_argument('--year_to', type=int, help='enter the year to', default=2023)
    parser.add_argument('--regexp', type=str, help='search movie by matching title', default='')
    return parser.parse_args()


def print_result():
     for line in csv.reader(sys.stdin):
        for key, value in do_map(line):
            print(key + "\t" + str(value))


def do_map(line):
    for key, value in sorted_list_line(line):
            yield key, value


def filter_by_year(year_from, year_to, string):
    pattern = r'\((\d{4})\)'
    if re.search(pattern, string):
        year = int(re.search(r'\((\d{4})\)', string).group(0)[1:-1])
        if year_from <= year <= year_to:
            return True


def check_by_regexp(name, string):
    pattern = name
    if re.search(pattern, string):
        return True


def filter_by_genres(genre, arg_genre):
    if arg_genre == '' and genre != '(no genres listed)':
        return True
    elif genre == arg_genre and genre != '(no genres listed)':
        return True


def sorted_list_line(list_line):
    if filter_by_year(args.year_from, args.year_to, list_line[1]) and check_by_regexp(args.regexp, list_line[1]):
        list_genres_argument = args.genres.split('|')
        genres = list_line[2].split('|')
        for arg_genre in list_genres_argument:
            for genre in genres:
                if filter_by_genres(genre, arg_genre):
                    key = genre
                    name = list_line[1][:-7]
                    year = int(re.search(r'\((\d{4})\)', list_line[1]).group(0)[1:-1])
                    yield key, (name, year)


if __name__ == "__main__":
    args = get_argpars()
    print_result()


