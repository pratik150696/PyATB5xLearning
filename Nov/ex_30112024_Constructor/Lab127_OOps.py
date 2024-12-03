count = 0


def increment():
    global count
    count = count + 1
    print(count)


increment()
increment()
increment()
increment()
print(count)
