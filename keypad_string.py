def keypad_string(keys):
    '''
    >>> keypad_string("12345")
    'adgj'
    >>> keypad_string("4433555555666")
    'hello'
    >>> keypad_string("2022")
    'a b'
    >>> keypad_string("")
    ''
    >>> keypad_string("111")
    ''
    >>> keypad_string("7773325550799984466666")
    'real python'
    '''

    keypad = {
            '1': '',
            '2': 'a',
            '22': 'b',
            '222': 'c',
            '3': 'd',
            '33': 'e',
            '333': 'f',
            '4': 'g',
            '44': 'h',
            '444': 'i',
            '5': 'j',
            '55': 'k',
            '555': 'l',
            '6': 'm',
            '66': 'n',
            '666': 'o',
            '7': 'p',
            '77': 'q',
            '777': 'r',
            '7777': 's',
            '8': 't',
            '88': 'u',
            '888': 'v',
            '9': 'w',
            '99': 'x',
            '999': 'y',
            '9999': 'z',
            '0': ' ',
            '': ''
    }

    s = ''
    res = ''
    for letter in keys:
        if len(s) > 0 and (s[-1] != letter or (s+letter) not in keypad):
            res += keypad[s]
            s = ''

        s += letter

    res += keypad[s]
    return res

