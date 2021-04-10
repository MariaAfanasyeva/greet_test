def list_handle(names_list, names_list_len, is_uppercase: bool):
    if is_uppercase:
        greeting_string = 'HELLO'
    else:
        greeting_string = 'Hello'
    for i, name in enumerate(names_list, 1):
        if i == names_list_len and names_list_len != 1:
            if is_uppercase:
                greeting_string += f" AND {name}!"
            else:
                greeting_string += f" and {name}."
        elif i == names_list_len and names_list_len == 1:
            if is_uppercase:
                greeting_string += f", {name}!"
            else:
                greeting_string += f", {name}."
        else:
            greeting_string += f", {name}"
    return greeting_string


def greet(*names):
    names_len = len(names)
    if names_len == 0:
        answer = 'Hello, my friend'
        return answer
    shouted_names = []
    simple_names = []
    for name in names:
        if not isinstance(name, str):
            raise ValueError("Wrong input")
        if name.isupper():
            shouted_names.append(name)
        else:
            simple_names.append(name)
    simple_names_len = len(simple_names)
    shouted_names_len = len(shouted_names)
    answer = ''
    if simple_names_len != 0:
        simple_string = list_handle(simple_names, simple_names_len, False)
        answer += simple_string

    if shouted_names_len != 0:
        shouted_string = list_handle(shouted_names, shouted_names_len, True)
        if answer:
            answer += 'AND ' + shouted_string
        else:
            answer += shouted_string
    return answer
