def greet(*names):
    if len(names) == 0:
        string = 'Hello, my friend'
    elif len(names) == 1:
        if names[0].isupper():
            string = 'HELLO, ' + names[0]
        else:
            string = 'Hello, ' + str(names[0])
    elif len(names) == 2:
        string = 'Hello, ' + names[0] + ' and ' + names[1]
    return string




