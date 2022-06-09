import pandas as pd
import argparse
import sys
import pyarrow.parquet as pq


def create_arg_parser():
    arg_parse = argparse.ArgumentParser(
        prog='converter.py',
        description='''Utility converse converts data from source file (csv-format) to destination
        file (parquet-format) and conversely'''
    )
    arg_parse.add_argument('--csv2parquet', nargs=2,
                           metavar=('<src-filename>', '<dst-filename>'),
                           help='convert csv-content to parquet-content')


    arg_parse.add_argument('--parquet2csv', nargs=2,
                           metavar=('<src-filename>', '<dst-filename>'),
                           help='convert parquet-content to csv-content')


    arg_parse.add_argument('--get-schema', nargs=1,
                           metavar='<filename>',
                           help='get schema of file: list of arguments and their types')


    return arg_parse


def run_csv2parquet(src_filename, dst_filename):
    df = pd.read_csv(src_filename, dtype=str)
    df.to_parquet(dst_filename)


def run_parquet2csv(src_filename, dst_filename):
    df = pd.read_parquet(src_filename)
    df.to_csv(dst_filename, index=False, encoding="UTF-8")


def run_get_schema(filename):
    suffix_csv = ".csv"
    suffix_parquet = ".parquet"

    if filename.endswith(suffix_csv):
        df = pd.read_csv(filename)
        print(df.dtypes)
    elif filename.endswith(suffix_parquet):
        pfile = pq.read_table(filename)
        print(format(pfile.schema))
    else:
        print("Wrong extension, try use file with .csv ot .parquet extension")


if __name__ == '__main__':
    parser = create_arg_parser()
    namespace = parser.parse_args(sys.argv[1:])

    if namespace.csv2parquet:
        run_csv2parquet(*namespace.csv2parquet)
    elif namespace.parquet2csv:
        run_parquet2csv(*namespace.parquet2csv)
    elif namespace.get_schema:
        run_get_schema(*namespace.get_schema)
    else:
        parser.print_help()





