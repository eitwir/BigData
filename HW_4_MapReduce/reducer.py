import sys
import argparse
import collections
import ast


def get_argpars():
    parser = argparse.ArgumentParser()
    parser.add_argument('--N', type=int, help='the number of movies you want to select')
    return parser.parse_args()


def check_by_n(N, genre, count):
    if N is None:
        return True
    else:
        count[genre] += 1
        if count[genre] <= N:
            return True


def reduce(key, values):
    count = collections.Counter()
    for name, year in values:
        if check_by_n(args.N, key, count):
            yield key, name, year


def print_result(data):
    print('genre; name; year')
    for line in data:
        genre, values = line.split('\t')
        values = ast.literal_eval(values)
        for key, name, year in reduce(genre, values):
            print(f'{key}; {name}; {year}')


if __name__ == "__main__":
    args = get_argpars()
    print_result(sys.stdin)
