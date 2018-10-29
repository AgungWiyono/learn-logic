while True:
    try:
        limit = int(input('How many row do you want?'))
        assert limit>0
        break
    except AssertionError:
        print("You can't print 0 line")
        print('')

for i in range(limit,-1,-1):
    print('{}*'.format(' '*i))
