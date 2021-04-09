def greet(*names):
    names_len = len(names)
    if names_len == 0:
        string = 'Hello, my friend'
        return string
    shouted_names = []
    simple_names = []
    for name in names:
        if not isinstance(name, str):
            raise ValueError("Wrong input")
        if name.isupper():
            shouted_names.append(name)
        else:
            simple_names.append(name)
    if names_len == 1:
        if names[0].isupper():
            string = 'HELLO, ' + names[0]
        else:
            string = 'Hello, ' + names[0]
    else:
        j = 0
        simple_names_len = len(simple_names)
        shouted_names_len = len(shouted_names)
        string = 'Hello '
        if simple_names_len == 1:
            string += ', ' + simple_names[0] + '.'
            string = string.replace(' ', '', 1)
        else:
            for simple_name in simple_names:
                string += simple_name + ' '
            string = string.strip()
            string_list = list(reversed(string.split()))
            string = ' and '.join(string_list)
            string = ' '.join(list(reversed(string.split())))
            string = string.replace(' and ', ', ', simple_names_len - 1)
            string += '.'

        if shouted_names_len != 0:
            shouted_string = 'HELLO '
            if shouted_names_len == 1:
                shouted_string += ', ' + shouted_names[0] + '!'
                shouted_string = shouted_string.replace(' ', '', 1)
            else:
                for shouted_name in shouted_names:
                    shouted_string += shouted_name + ' '
                shouted_string = shouted_string.strip()
                shouted_string_list = list(reversed(shouted_string.split()))
                shouted_string = ' AND '.join(shouted_string_list)
                shouted_string = ' '.join(list(reversed(shouted_string.split())))
                shouted_string = shouted_string.replace(' AND ', ', ', shouted_names_len - 1)
                shouted_string += '!'
            string += 'AND ' + shouted_string
    return string

