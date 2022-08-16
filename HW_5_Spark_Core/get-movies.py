import pyspark
import re
import argparse


def get_argpars():
    parser = argparse.ArgumentParser()
    parser.add_argument('--N', type=int, help='the number of movies you want to select')
    parser.add_argument('--genres', type=str, help='enter the genres you want to see', default='')
    parser.add_argument('--year_from', type=int, help='enter the year from', default=1900)
    parser.add_argument('--year_to', type=int, help='enter the year to', default=2023)
    parser.add_argument('--regexp', type=str, help='search movie by matching title', default='')
    return parser.parse_args()


def get_list_line_from_original_string(original_line):
    movieID, title_genres = original_line.split(',', maxsplit=1)
    title, genres = title_genres.rsplit(',', maxsplit=1)
    if '"' in title:
        title = title[1:-1]
    movie = [movieID, [title, genres]]
    return movie


def filter_by_regexp(line):
    _,(title,_) = line
    pattern = args.regexp
    if re.search(pattern, title):
        return True


def filter_by_year(line):
    _,(title,_) = line
    pattern = r'\((\d{4})\)'
    if re.search(pattern, title):
        year = int(re.search(r'\((\d{4})\)', title).group(0)[1:-1])
        if args.year_from <= year <= args.year_to:
            return True


def get_reorgonize_movies_rdd():
    original_movies_rdd = sc.textFile('./files/movies.csv')
    list_line_movies_rdd = original_movies_rdd.map(lambda string: get_list_line_from_original_string(string))
    movies_rdd = list_line_movies_rdd.filter(lambda list: filter_by_regexp(list) and filter_by_year(list))
    return movies_rdd


def get_list_from_rating_string(string):
    _,movieId,rating,_ = string.split(',')
    return [movieId, float(rating)]


def get_reorgonize_rating_rdd():
    # original rating rdd without header
    original_rating_rdd = sc.textFile('./files/ratings.csv').filter(lambda x: x.split(',')[1] != 'movieId')
    list_line_rating_rdd = original_rating_rdd.map(lambda string: get_list_from_rating_string(string))
    grouped_rating_rdd = list_line_rating_rdd.groupByKey()
    rating_rdd = grouped_rating_rdd.map(lambda x: [x[0], round(sum(x[1]) / len(x[1]), 2)])
    return rating_rdd


def get_joined_rdd(movies_rdd, rating_rdd):
    joined_rdd = movies_rdd.join(rating_rdd)
    return joined_rdd


def filter_by_genres(genre, arg_genre):
    if arg_genre == '' and genre != '(no genres listed)':
        return True
    elif genre == arg_genre and genre != '(no genres listed)':
        return True


def reorgonize_line(line):
    _,((name_with_year, genres), rating) = line

    year = int(re.search(r'\((\d{4})\)', name_with_year).group(0)[1:-1])
    name = name_with_year[:-7]

    for genre in genres.split('|'):
        for arg_genre in args.genres.split('|'):
            if filter_by_genres(genre, arg_genre) :
                yield [genre, [name, year, rating]]


def get_reorgonize_joined_rdd(joined_rdd):
    reorgonize_joined_rdd = joined_rdd.flatMap(reorgonize_line)
    # sort_by: genres, ratings, year, name
    sorted_reorgonize_joined_rdd = reorgonize_joined_rdd.sortBy(lambda x: (x[0], -x[1][2], -x[1][1], x[1][0]))
    grouped_joined_rdd = sorted_reorgonize_joined_rdd.groupByKey()
    # x[0] == genre
    result_reorgonize_rdd = grouped_joined_rdd.sortBy(lambda x: x[0])
    return result_reorgonize_rdd


def get_n(line):
    N = args.N
    if N is None:
        return len(line)
    else:
        if N <= len(line):
            return N
        elif N > len(line):
            return len(line)


def check_by_n(line):
    genre, values = line

    for name, year, rating in list(values)[:get_n(values)]:
        yield f'{genre}; {name}; {year}; {rating}'


def get_result_rdd(reorgonize_joined_rdd):
    result = reorgonize_joined_rdd.flatMap(check_by_n)
    return result


def main():
    movies_rdd = get_reorgonize_movies_rdd()
    rating_rdd = get_reorgonize_rating_rdd()
    joined_rdd = get_joined_rdd(movies_rdd, rating_rdd)
    reorgonize_joined_rdd = get_reorgonize_joined_rdd(joined_rdd)
    result = get_result_rdd(reorgonize_joined_rdd)
    result.saveAsTextFile('result')


if __name__ == "__main__":
    args = get_argpars()
    sc = pyspark.SparkContext(appName="myAppName")
    main()
