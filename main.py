def make_world_go_round(world, speed, happy=True):
    print("The {} is going round at speed {} knots".format(world, speed))


# arguments unpacking
def some_generic_fn(a, *args, c, **kwargs):
    print("a: {}".format(a))
    print("Args: {}".format(args))
    print("Kwargs: {}".format(kwargs))


def main():
    # make_world_go_round("Earth", 120)
    make_world_go_round(speed=120, happy=False, world="Earth")
    make_world_go_round("Earth", speed=120)
    # make_world_go_round(speed=120, "Earth")  # не работает,
    # неименованные нельзя после хоть  1го  именованного
    make_world_go_round(speed=120, world="Earth")  # работает

    some_generic_fn(5, 3, 'a', s='s', t=[1, 2], f=(5+3), c='just a string')
    # some_generic_fn(5, 3, 'a', s='s', [1, 2], f=(5+3))  # не работает

main()
