"""
    Лексический анализатор
    на конечных автоматах
"""


import string


next_state = {
    0: {
        ":": 1,
        "=": 5,
        "-": 3,
        "+": 8,
        "/": 7,
        "*": 9,
        "&": 11,
        "|": 13,
        "<": 16,
        ">": 18,
        r"\d": 19,
        "t": 21,
        "f": 26,
        "i": 31,
        "(": 64,
        "[": 55,
        r"\w": 47,
        "e": 38,
        "l": 42,
        "b": 51,
    },
    1: {
        ":": 72
    },
    # S2 - stop
    3: {
        " ": 10,
        ">": 4
    },
    4: {
        " ": 2
    },
    5: {
        " ": 6,
        "=": 17
    },
    # S6 - stop
    7: {
        " ": 10
    },
    8: {
        " ": 10
    },
    9: {
        " ": 10,
        "=": 17
    },
    # S10 - stop
    11: {
        "&": 12
    },
    12: {
        " ": 15
    },
    13: {
        "|": 14
    },
    14: {
        " ": 15
    },
    # S15 - stop
    16: {
        " ": 17
    },
    18: {
        " ": 17
    },
    19: {
        r"\d": 19,
        " ": 20
    },
    # S20 - stop
    21: {
        "r": 22,
        "h": 34
    },
    22: {
        "u": 23
    },
    23: {
        "e": 24
    },
    24: {
        " ": 25
    },
    # S25 - stop
    26: {
        "a": 27
    },
    27: {
        "l": 28
    },
    28: {
        "s": 29
    },
    29: {
        "e": 30
    },
    30: {
        " ": 25
    },
    31: {
        "f": 32,
        "n": 46
    },
    32: {
        " ": 37
    },
    # S33 - null
    34: {
        "e": 35
    },
    35: {
        "n": 36
    },
    36: {
        " ": 37
    },
    # S37 - stop
    38: {
        "l": 39
    },
    39: {
        "s": 40
    },
    40: {
        "e": 41
    },
    41: {
        " ": 37
    },
    42: {
        "e": 43
    },
    43: {
        "t": 44
    },
    44: {
        " ": 37
    },
    45: {
        "n": 46
    },
    46: {
        " ": 37,
        "t": 49
    },
    47: {
        r"\w": 47,
        r"\d": 47,
        " ": 48
    },
    # S48 - stop
    49: {
        " ": 50
    },
    # S50 - stop
    51: {
        "o": 52
    },
    52: {
        "o": 53
    },
    53: {
        "l": 54
    },
    54: {
        " ": 50
    },
    55: {
        "i": 56,
        "b": 60
    },
    56: {
        "n": 57
    },
    57: {
        "t": 58
    },
    58: {
        "]": 59
    },
    59: {
        " ": 50
    },
    60: {
        "o": 61
    },
    61: {
        "o": 62
    },
    62: {
        "l": 63
    },
    63: {
        "]": 59
    },
    64: {
        "i": 65,
        "b": 68
    },
    65: {
        "n": 66
    },
    66: {
        "t": 67
    },
    67: {
        ")": 73,
        ",": 64
    },
    68: {
        "o": 69
    },
    69: {
        "o": 70
    },
    70: {
        "l": 71
    },
    71: {
        ")": 73,
        ",": 64
    },
    72: {
        " ": 2
    },
    73: {
        " ": 50
    }
}


def state_machine():
    global lex_val
    global DBG
    lex_val = ""
    cur_state = 0
    cur_input = recognize()
    set_end_states = {2, 6, 10, 15, 17, 20, 25, 37, 48, 50}
    while (cur_state not in set_end_states) and (cur_input != "endf"):
        if DBG:
            print("cur_input = {0}\ncur_state = {1}\n".format(cur_input, cur_state))
        try:
            cur_state = next_state[int(cur_state)][cur_input]
        except KeyError:
            raise Exception("Лексическая ошибка !")
        if cur_state not in set_end_states:
            cur_input = recognize()
    if (cur_state not in set_end_states) and (cur_input == "endf"):
        raise Exception("Лексическая ошибка !")
    elif cur_state == 2:
        return "spec_sym"
    elif cur_state == 6:
        return "op_asgm"
    elif cur_state == 10:
        return "op_arif"
    elif cur_state == 15:
        return "op_log"
    elif cur_state == 17:
        return "op_cmp"
    elif cur_state == 20:
        return "const_int"
    elif cur_state == 25:
        return "const_bool"
    elif cur_state == 37:
        return "keyw"
    elif cur_state == 48:
        return "id"
    elif cur_state == 50:
        return "type"


def recognize():
    global lex_val
    global entry
    if entry == "":
        result = "endf"
    else:
        if entry[0] in "+-*/&|<>=,:([]) " or entry[0] in string.ascii_lowercase:
            result = entry[0]
        elif entry[0] in string.digits:
            result = r"\d"
        elif entry[0] in string.ascii_uppercase:
            result = r"\w"
        else:
            result = "error"
        lex_val += entry[0]
        entry = entry[1:]
    return result


# DBG = not True
#entry = "F 1 Y = 123 G X Y 123 = true "
# entry = "F X = let G Y = if X > Y && X > 0 then X else Y in G 2 + 8080 * 5 "
# entry = "MAX :: int "
# entry = "MAX :: int -> bool FOO :: bool -> int -> [int] -> (int,int,bool,int) "
while entry != "":
        print("{0} '{1}'".format(state_machine(), lex_val.strip()))
