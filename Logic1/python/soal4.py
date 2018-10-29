while True:
    try:
        size = int(input('How many row do you want?'))
        assert size>0
        break
    except AssertionError:
        print("You can't print 0 line")
        print('')

for i in range(size):
    if i==size//2:
        print('*'*size)
    else:
        print(''.join('*' if j==i or j==size-1-i or j==size//2 else ' ' for j in range(size)))
