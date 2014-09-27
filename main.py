import random


def main():
    for i in range(128):
        r = random.randrange(0, 1024)
        if r % 5 == 0:
            print(r, end=', ')

main()
