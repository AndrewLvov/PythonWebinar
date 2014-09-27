import random


def happy_toad():
    h = "toad!"
    # print("{}: {}".format(h, str(type(h))))
    h = ['t', 'o', 'a', 'd']
    # print("{}: {}".format(h, type(h)))
    print("I'm a happy {}".format(h))
    # print(type("I'm a happy {}".format(h)))
    return 0


def main():
    for i in range(32):
        # print("i: {}".format(type(i)))
        r = random.randrange(0, 1024)
        # print("r: {}".format(type(r)))
        print(r)
        if r % 5 == 0:
            # print("r % 5 == 0: {}".format(type(r % 5 == 0)))
            happy_toad()

main()
