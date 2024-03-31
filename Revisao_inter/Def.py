x = 1


def escopo():
    global x
    print(x)


print(x)
escopo()
