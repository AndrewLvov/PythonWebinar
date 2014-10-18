
def main():
    # n1 = 1
    # n2 = 1
    # print(n1)
    # for i in range(14):
    #     with open('{}.txt'.format(i), 'w') as f:
    #         f.write(str(n1))
    #     n1, n2 = n2, n1 + n2

    # zfill
    # format

    # nums = sorted(['{:04}'.format(i) for i in range(14)])

    # nums = sorted(
    #     map(lambda x: x.zfill(4),
    #         [str(i) for i in range(14)])
    # )
    # аналог:
    nums = []
    for i in range(14):
        v = str(i)
        v = v.zfill(4)
        nums.append(v)
    nums = sorted(nums)
    print(nums)

main()
