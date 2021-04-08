def greet(name=None):
    if name is None:
        string = 'Hello, my friend'
    else:
        if isinstance(name, str):
            if name.isupper():
                string = 'HELLO, ' + name
            else:
                string = 'Hello, ' + name
        else:
            string = 'Wrong input'
    return string

