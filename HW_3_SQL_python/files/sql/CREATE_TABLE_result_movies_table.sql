use movies_db;

create table        result_movies_table as

select distinct     movies.movie_id,
                    movies.genres,
                    movies.title,
                    movies.year,
                    avg_rating.avgrating

from                movies

join                avg_rating

on                  movies.movie_id = avg_rating.movie_id

order by            movies.movie_id,
                    movies.genres,
                    avg_rating.avgrating desc;



delete from         result_movies_table

where               genres = '(no genres listed)'
                    or title = ''
                    or title = '''71 '
                    or `year` = 0;