import numpy as np


def test1():
    arr = np.zeros(10)
    print(arr)

    arr = np.ones(10)
    print(arr)

    arr = np.full(10, 5.)
    print(arr)

    arr = np.full(10, 5.)
    print(arr)

    arr = np.arange(10, 51)
    print(arr)

    arr = np.arange(10, 51, 2)
    print(arr)

    arr = np.random.randint(0, 9, 9).reshape((3, 3))
    print(arr)

    arr = np.eye(3)
    print(arr)

    arr = np.random.rand(1)  # Gaussian Distribution
    print(arr)

    arr = np.random.randn(4)  # Gaussian Distribution
    print(arr)

    arr = np.arange(0, 101) / 100
    print(arr)

    arr = np.linspace(0, 1, 20)
    print(arr)


def test2():
    arr = np.arange(1, 26).reshape(5, 5)
    print('Matrix :')
    print(arr)
    print('Result of Slice :')
    print(arr[2:, 1:])
    print(arr[3, 4])
    print(arr[0:3, 1:2])
    print(arr[4])
    print(arr[3:])
    print(np.sum(arr))
    print(np.std(arr))
    print(np.sum(arr, axis=0))


