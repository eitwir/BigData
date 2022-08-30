import argparse
from config import host, user, passwd, db_name
import pymysql
from pymysql.constants import CLIENT
from pymysql import Error
import time


start_time = time.time()


def get_argpars():
    parser = argparse.ArgumentParser()
    parser.add_argument('--N', type=int, help='the number of movies you want to select')
    parser.add_argument('--genres', type=str, help='enter the genres you want to see', default='')
    parser.add_argument('--year_from', type=int, help='enter the year from', default=1900)
    parser.add_argument('--year_to', type=int, help='enter the year to', default=2023)
    parser.add_argument('--regexp', type=str, help='search movie by matching title', default='')
    return parser.parse_args()


def get_connection_to_db(host, user, passwd, db_name):
    connection = None
    try:
        connection = pymysql.connect(
            host=host,
            user=user,
            passwd=passwd,
            database=db_name,
            client_flag=CLIENT.MULTI_STATEMENTS
        )
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


def print_result(connection, sql_script_path, args):
    print('genre; title; year; rating')
    genres = args.genres.split("|")

    for genre in genres:
        with connection.cursor() as cursor:
            with open(sql_script_path) as file:
                script = file.read()
                cursor.execute(script.format(year_from=args.year_from,
                                             year_to=args.year_to,
                                             name=str(args.regexp),
                                             genre=str(genre),
                                             N=args.N))
                rows = cursor.fetchall()
                for row in rows:
                    print(f'{row[0]}; {row[1]}; {row[2]}; {row[3]}')


if __name__ == "__main__":
    args = get_argpars()
    connection = get_connection_to_db(host, user, passwd, db_name)
    print_result(connection, r'./files/sql/GET_RESULT.sql', args)


print("--- %s seconds ---" % (time.time() - start_time))
