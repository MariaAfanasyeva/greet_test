def greet(name=None):
    if name is None:
        string = 'Hello, my friend'
    else:
        string = 'Hello, ' + str(name)
    return string
