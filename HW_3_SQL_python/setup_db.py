import pymysql
from pymysql import Error
from pymysql.constants import CLIENT
import csv
import re


def create_connection_to_server_and_create_db(host, user, passwd, sql_script_path):
    try:
        connection = pymysql.connect(
            host=host,
            user=user,
            passwd=passwd,
            client_flag=CLIENT.MULTI_STATEMENTS
        )
        try:
            with connection.cursor() as cursor:
                with open(sql_script_path, newline='') as file:
                    script = file.read()
                    cursor.execute(script)
            connection.commit()
            print('Database was create')
        except Error as e:
            print(f"The error '{e}' occurred")
    except Error as e:
        print(f"The error '{e}' occurred")


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
        print('Connection to Database successful')
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection


def create_table(connection, sql_script_path):
    try:
        with connection.cursor() as cursor:
            with open(sql_script_path, newline='') as file:
                script = file.read()
                cursor.execute(script)
            connection.commit()
    except Error as e:
        print(f"The error '{e}' occurred")


def get_list_from_csv_file(csv_file_path):
    data = []
    with open(csv_file_path, newline='') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            data.append(row)
    result_data = data[1:]
    return result_data


def fill_movies_table(connection, movies_data, sql_script_path):
    with connection.cursor() as cursor:
        for movie_id, title, genres in movies_data:
            if re.search(r'\((\d{4})\)', title) is not None:
                search_year = re.search(r'\((\d{4})\)', title)
                result_year = search_year.group(0)[1:-1]
                year = int(result_year)
            else:
                year = 0
            list_genres = genres.split('|')
            for genre in list_genres:
                with open(sql_script_path) as file:
                    script = file.read()
                    cursor.execute(script.format(int(movie_id), connection.escape(title[:-7]), int(year),
                                                 connection.escape(genre)))
                connection.commit()


def fill_rating_table(connection, rating_data, sql_script_path):
    with connection.cursor() as cursor:
        for _, movie_id, rating , _ in rating_data:
            with open(sql_script_path) as file:
                filling_script = file.read()
                cursor.execute(filling_script.format(int(movie_id), float(rating)))
        connection.commit()


if __name__ == "__main__":
    create_connection_to_server_and_create_db('localhost',
                                              'root',
                                              '1234567890',
                                              r'./files/sql/CREATE_DATABASE_movies_db.sql')
    connection = get_connection_to_db('localhost', 'root', '1234567890', 'movies_db')
    movies = get_list_from_csv_file('./Data/movies.csv')
    rating = get_list_from_csv_file('./Data/ratings.csv')
    create_table(connection, './files/sql/CREATE_TABLE_movies.sql')
    create_table(connection, './files/sql/CREATE_TABLE_rating.sql')
    fill_movies_table(connection, movies, './files/sql/FILL_MOVIES_TABLE.sql')
    fill_rating_table(connection, rating, './files/sql/FILL_RATING_TABLE.sql')
    create_table(connection, './files/sql/CREATE_TABLE_avg_rating.sql')
    create_table(connection, './files/sql/CREATE_TABLE_result_movies_table.sql')
