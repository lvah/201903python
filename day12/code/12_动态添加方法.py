
def show():
    print('show.....')

Date = type('Date', (), {'show': show})
Date.show()



