import sys
import ast


def get_dict(data):
    result = ''

    for line in data:
        result += line
    return ast.literal_eval(result)


def dict_sorted_by_key(dict_data):
    sorted_result = sorted(dict_data.items(), key=lambda x: x[0])
    dict_result = dict(sorted_result)
    return dict_result


def dict_sorted_by_values(dict):
    result = {}
    for key in dict:
        result[key] = (sorted(map(ast.literal_eval, dict[key]), key=lambda x: (x[1], x[0]), reverse=True))
    return result


if __name__ == "__main__":
    my_dict = get_dict(sys.stdin)
    sorted_dict_by_genre = dict_sorted_by_key(my_dict)
    sorted_dict = dict_sorted_by_values(sorted_dict_by_genre)
    for key in sorted_dict:
        print(key + "\t" + str(sorted_dict[key]))


