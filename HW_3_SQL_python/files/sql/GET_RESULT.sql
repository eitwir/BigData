select      genres,
            title,
            `year`,
            round(avgrating, 2) as avgrating

from       result_movies_table

where
            `year` between {year_from} and {year_to}
            and title like "%{name}%"
			and genres like "%{genre}%"

order by    genres,
            avgrating desc, `year` desc, title

limit       {N};
