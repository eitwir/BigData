# **FILTER MOVIES**
This console utility allows you to find films by the highest rating with the set parameters.
***
# TECH
- [argparser](https://docs.python.org/3/library/argparse.html) — Parser for command-line options, arguments and sub-commands.
- [collections](https://pythonworld.ru/moduli/modul-collections.html) — provides specialized data types based on dictionaries, tuples, sets, lists.
- [csv](https://pythonworld.ru/moduli/modul-csv.html) — reading and writing CSV files.
- [re](https://tproger.ru/translations/regular-expression-python/) — regular expressions.
***
# USAGE
Script workflow:

`get-movies.py [--N <int>] | [--genres <name_genre|name_genre>] | [--year_from <int> ] | [--year_to <int> ] | [--regexp <films name>]`

## Prerequisites

What things you need to install the software and how to install them:

```
pip -r reqirements.txt
```

***

# OPTIONS

    * --N [the number of movies you want to select.]
    * --genres [enter the genres you want to see. It can be multiple. For example: Comedy|Adventure]
    * --year_from [enter the year from.]
    * --year_to [enter the year to.] 
    * --regexp [search movie by matching title.] 

***

# EXAMPLES

```
* get-movies.py --N 3 --year_from 2000 --year_to 2005  --genres 'Action' 

    # console return:

    genre; name; year; rating
    Action; Battle Royale 2: Requiem (Batoru rowaiaru II: Chinkonka); 2003; 5.0
    Action; Sisters (Syostry); 2001; 5.0
    Action; Dog Soldiers; 2002; 4.7


* get-movies.py --N 3 --year_from 1995 --year_to 2001 --genres 'Adventure|Action' 

    # console return:

    genre; name; year; rating
    Action; Sisters (Syostry); 2001; 5.0
    Action; Knock Off; 1998; 5.0
    Action; Assignment, The; 1997; 5.0
    Adventure; The Love Bug; 1997; 5.0
    Adventure; Musa the Warrior (Musa); 2001; 4.5
    Adventure; Dragonheart 2: A New Beginning; 2000; 4.5
```
***
# NOTE
You can download the data from the link: https://files.grouplens.org/datasets/movielens/ml-latest-small.zip