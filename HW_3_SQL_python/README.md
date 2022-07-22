# **FILTER MOVIES WITH SQL**
This console utility allows you to find films by the highest rating with the set parameters.
***

# TECH
- [argparser](https://docs.python.org/3/library/argparse.html) — Parser for command-line options, arguments and sub-commands.
- [pymysql](https://pypi.org/project/PyMySQL/#id6) — PyMySQL is an interface for connecting to a MySQL database server from Python. It implements the Python Database API v2.0 and contains a pure-Python MySQL client library.
- [csv](https://pythonworld.ru/moduli/modul-csv.html) — reading and writing CSV files.
- [re](https://tproger.ru/translations/regular-expression-python/) — regular expressions.

# **Usage:**

Script workflow:

1. `setup_db.py`
2. `get-movies.py [--N <int>] | [--genres <name_genre|name_genre>] | [--year_from <int> ] | [--year_to <int> ] | [--regexp <films name>]`

***

# **OPTIONS:**


```
    * --N [the number of movies you want to select.]
    * --genres [enter the genres you want to see. It can be multiple. For example: Comedy|Adventure]
    * --year_from [enter the year from.]
    * --year_to [enter the year to.] 
    * --regexp [search movie by matching title.] 

```


***

# **EXAMPLES:**

```
python get-movies.py --N 10 --genres "Comedy" --year_from 1999 --year_to 2005
 
 # console return:
 
genre; title; year; rating
Comedy; Boy Eats Girl ; 2005; 5.00
Comedy; George Carlin: Life Is Worth Losing ; 2005; 5.00
Comedy; Guy X ; 2005; 5.00
Comedy; Stuart Little 3: Call of the Wild ; 2005; 5.00
Comedy; Alesha Popovich and Tugarin the Dragon ; 2004; 5.00
Comedy; Calcium Kid, The ; 2004; 5.00
Comedy; Dylan Moran: Monster ; 2004; 5.00
Comedy; Go for Zucker! (Alles auf Zucker!) ; 2004; 5.00
Comedy; Palindromes ; 2004; 5.00
Comedy; Saving Face ; 2004; 5.00


python get-movies.py --N 7 --genres "Action|Adventure" --year_from 2004 --year_to 2008

 # console return:

genre; title; year; rating
Action; Love Exposure (Ai No Mukidashi) ; 2008; 5.00
Action; Max Manus ; 2008; 5.00
Action; Tekkonkinkreet (Tekkon kinkurîto) ; 2006; 4.63
Action; Assembly (Ji jie hao) (; 2007; 4.50
Action; Doctor Who: Voyage Of The Damned ; 2007; 4.50
Action; Rise of the Footsoldier ; 2007; 4.50
Action; Tae Guk Gi: The Brotherhood of War (Taegukgi hwinalrimyeo) ; 2004; 4.50
Adventure; Asterix and the Vikings (Astérix et les Vikings) ; 2006; 5.00
Adventure; The Fox and the Hound 2 ; 2006; 5.00
Adventure; Palindromes ; 2004; 5.00
Adventure; Tekkonkinkreet (Tekkon kinkurîto) ; 2006; 4.63
Adventure; BURN-E ; 2008; 4.50
Adventure; Golden Door (Nuovomondo) ; 2006; 4.50
Adventure; Jack-Jack Attack ; 2005; 4.50


*  python get-movies.py --N 3 --genres "Drama"    

 # console return:

genre; title; year; rating
Drama; Loving Vincent ; 2017; 5.00
Drama; All Yours ; 2016; 5.00
Drama; Indignation ; 2016; 5.00
```
***

# NOTE
You can download the data from the link: https://files.grouplens.org/datasets/movielens/ml-latest-small.zip

