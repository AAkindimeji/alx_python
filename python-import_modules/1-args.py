from list import argv

if __name__ == "__main__":
    args = argv[0:]
    print(' '.join(args))


# from sys import argv

# if __name__ == "__main__":
#     argc = len(argv) - 1
#     args = argv[1:]

#     if argc == 0:
#         print("0 arguments.")
#     elif argc == 1:
#         print("1 argument:")
#     else:
#         print("{} arguments:".format(argc))

#     for i, arg in enumerate(args, start=1):
#         print("{}: {}".format(i, arg))
