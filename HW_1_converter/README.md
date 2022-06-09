# CONVERTER

Converter is a console app to convert files from csv-format to parquet-format and conversely.

### Features

- csv-to-parquet file converting mode
- parquet-to-csv file converting mode
- getting file schema (list of arguments and their types)

## Tech

Converter uses a number of open source projects to work properly:

- [pandas](https://pandas.pydata.org/) — Software library in Python for data processing and analysis.
- [argparser](https://docs.python.org/3/library/argparse.html) — Parser for command-line options, arguments and sub-commands
- [pyarrow.parquet](https://arrow.apache.org/docs/python/parquet.html) — The Apache Parquet project provides a standardized open-source columnar storage format for use in data analysis systems.
- [sys](https://docs.python.org/3/library/sys.html) — This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.


## Usage

For csv-to-parquet file converting mode:


```sh
converter.py --csv2parquet <src-filename> <dst-filename>
```
For parquet-to-csv file converting mode:

```sh
converter.py --parquet2csv <src-filename> <dst-filename>
```

For getting file schema:

```sh
converter.py --get-schema <filename>
```

For getting help:

```sh
converter.py --h, --help
```

### Note

This console application can only use files with extension .csv or .parquet to get schema.


