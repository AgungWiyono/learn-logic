while True:
    try:
        size = int(input('How many row do you want?'))
        assert size>0
        break
    except AssertionError:
        print("You can't print 0 line")
        print('')

for i in range(size):
    print(''.join('*' if j==i or j==size-1-i else ' ' for j in range(size)))
