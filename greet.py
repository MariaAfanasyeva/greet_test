def greet(*names):
    if len(names) == 0:
        string = 'Hello, my friend'
    elif len(names) == 1:
        if isinstance(names[0], str):
            if names[0].isupper():
                string = 'HELLO, ' + names[0]
            else:
                string = 'Hello, ' + names[0]
        else:
            string = 'Wrong input'
    elif len(names) == 2:
        for name in names:
            if not isinstance(name, str):
                string = 'Wrong input'
                return string
        string = 'Hello, ' + names[0] + ' and ' + names[1]
    return string




