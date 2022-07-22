# **Description:**

Dir homework3 is a command-line utility that determines the most rated films (by average rating) for each specified genre (if the genre is passed as an argument of the command line).
The utility return to the console: genre, title, year of release and rating.

***

# **Usage:**


First you need to deploy the server.

```
python3 server/setup_db.py
```

After deploying the server, you can already use the console utility get-movies.py:

```
python3 client/get-movies.py [-N <int>] | [-genres <name_genre|name_genre>] | [-year_from <int> ] | [-year_to <int> ] | [-regexp <films name>]
```

***

# **OPTIONS:**


```
    * -N [count of the highest rated films for each genre.]
    * -genres [filter by genre, set by the user. it can be multiple. For example: Comedy|Adventure or Comedy&Adventure.]
    * -year_from [filter for the years of release of films.]
    * -year_to [filter for the years of release of films.]
    * -regexp [filter (regular expression) on the movie name.]
```


***

# **EXAMPLES:**

```

* python3 client/get-movies.py -N 4 -genres 'Action'


    # console return:

    genre;title;year;rating
    Action;Tombstone ;1993;5.00
    Action;Star Wars: Episode IV - A New Hope ;1977;5.00
    Action;Rob Roy ;1995;5.00
    Action;Desperado ;1995;5.00




*  python3 client/get-movies.py -N 4 -genres 'Drama|Adventure' -year_from 2015 -year_to 2020


    # console return:

    genre;title;year;rating
    Drama;Wonder ;2017;5.00
    Drama;Inside Out ;2015;5.00
    Drama;Three Billboards Outside Ebbing, Missouri ;2017;5.00
    Drama;The Martian ;2015;5.00
    Adventure;Mad Max: Fury Road ;2015;5.00
    Adventure;Rogue One: A Star Wars Story ;2016;5.00
    Adventure;Spectre ;2015;5.00
    Adventure;Star Wars: Episode VII - The Force Awakens ;2015;5.00




*  python3 client/get-movies.py -regexp Love -N 3 -genres 'Romance'


    # console return:

    genre;title;year;rating
    Romance;Only Lovers Left Alive ;2013;5.00
    Romance;Love Actually ;2003;5.00
    Romance;Everyone Says I Love You ;1996;5.00


```

***