import random


def main():
    for i in range(128):
        print(random.randrange(0, 1024), end=', ')

main()
