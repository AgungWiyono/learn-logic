import math

while True:
    try:
        size = int(input('How many row do you want?'))
        assert size>0
        break
    except AssertionError:
        print("You can't print 0 line")
        print('')

median = int(math.ceil(size/2))
for i in range(0,median+1):
    print('{}{}'.format(' '*i, '*'*(size-i*2)))
for i in range(median-1, -1,-1):
    print('{}{}'.format(' '*i, '*'*(size-i*2)))
