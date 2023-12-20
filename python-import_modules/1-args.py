import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    num_args = len(args)

    print("{} argument{}{}".format(
        num_args,
        's' if num_args != 1 else '',
        ':' if num_args > 0 else '.'
    ))

    for i, arg in enumerate(args, start=1):
        print("{}: {}".format(i, arg))

