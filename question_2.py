before = 0
after = 0

while after < 77:
    print(after)
    after = after + before
    before = after - before

    if after == 0:
        after = after + 1
