def printNos(N):
    if N == 0:
        return

    printNos(N - 1)

    print(N)


if __name__ == '__main__':
    printNos(5)
