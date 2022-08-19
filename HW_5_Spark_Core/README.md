# **FILTER MOVIES WITH SPARK CORE LOCAL**
This console utility allows you to find films by the highest rating with the set parameters.
***

# USAGE
Script workflow:

`./get-movies.sh [--N --genres --year_from --year_to --regexp]`

***

# **OPTIONS:**

    * --N [the number of movies you want to select.]
    * --genres [enter the genres you want to see. It can be multiple. For example: Comedy|Adventure]
    * --year_from [enter the year from.]
    * --year_to [enter the year to.] 
    * --regexp [search movie by matching title.] 

***

# EXAMPLES

```
* ./get-movies.sh --N 3 --genres 'Action --year_from 2000 --year_to 2005' 

    # console return:

    genre; name; year; rating
    Action; Battle Royale 2: Requiem (Batoru rowaiaru II: Chinkonka); 2003; 5.0
    Action; Sisters (Syostry); 2001; 5.0
    Action; Dog Soldiers; 2002; 4.7


* ./get-movies.sh --N 3 --genres 'Adventure|Action --year_from 1995 --year_to 2001 ' 

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