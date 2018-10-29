while True:
    try:
        size = int(input('How many row do you want?'))
        assert size>0
        break
    except AssertionError:
        print("You can't print 0 line")
        print('')

for i in range(1,size+1):
    print('*'*i)
