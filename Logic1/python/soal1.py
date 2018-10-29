while True:
    try:
        size = int(input('How many row do you want?'))
        assert size>0
        assert type(size)==int
        break
    except AssertionError:
        print("Please enter number bigger than 0")
        print('')

for i in range(size):
    print('{}*'.format(' '*i))
