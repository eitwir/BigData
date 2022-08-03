import sys


def shuffle(data):
    result = {}
    for line in data:
        key, value = line.split("\t")

        value = value[:-1]

        if key not in result:
            result[key] = []
            result[key].append(value)
        elif key in result:
            result[key].append(value)

    return result


if __name__ == "__main__":
    print(shuffle(sys.stdin))
