use movies_db;

create table rating (
id              INT                 AUTO_INCREMENT,
movie_id        INT                 not null,
rating          DECIMAL(3, 2),
primary key     (id)
);