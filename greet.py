def greet(*names):
    if len(names) == 0:
        string = 'Hello, my friend'
        return string
    else:
        for name in names:
            if not isinstance(name, str):
                string = 'Wrong input'
                return string
        if len(names) == 1:
            if names[0].isupper():
                string = 'HELLO, ' + names[0]
            else:
                string = 'Hello, ' + names[0]
        else:
            string = 'Hello, ' + names[0] + ' and ' + names[1]
    return string




