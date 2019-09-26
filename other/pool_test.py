import multiprocessing
pool = multiprocessing.Pool(5)


def f(x):
    return x * x


if __name__ == '__main__':
    # with pool as p:
        # print(p.map(f, [1, 2, 3, 5, 7]))
    print(map(f, [1, 2, 3]))
