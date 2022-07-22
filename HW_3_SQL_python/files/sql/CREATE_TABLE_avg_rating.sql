use movies_db;

create table avg_rating as

select distinct     movie_id,
                    avg(rating) as avgrating

from                rating

group by            movie_id

order by            movie_id;