use movies_db;

create table if not exists rating 
(
id              INT                 AUTO_INCREMENT,
movie_id        INT                 NOT NULL,
rating          DECIMAL(3, 2),
primary key     (id)
);