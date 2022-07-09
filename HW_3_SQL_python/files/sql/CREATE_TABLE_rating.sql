use movies_db;

create table rating (
id              INT                 auto_increment,
movie_id        INT                 not null,
rating          DECIMAL(3, 2),
primary key    (id)
);