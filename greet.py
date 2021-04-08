def greet(name=None):
    if name is None:
        string = 'Hello, my friend'
    else:
        if name.isupper():
            string = 'HELLO, ' + name
        else:
            string = 'Hello, ' + str(name)
    return string

