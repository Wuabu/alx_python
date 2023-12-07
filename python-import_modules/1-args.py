import sys

if __name__ == "__main__":
    argv_len = len(sys.argv) - 1

    print("{} argument{}{}{}".format(
        argv_len,
        's' if argv_len != 1 else '',
        ':' if argv_len > 0 else '.',
        '\n' if argv_len > 0 else ''
    ))

    for i, arg in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(i, arg))
