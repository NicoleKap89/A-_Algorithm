
def base_heuristic(_pancake_state):
    pancake_lst_int = _pancake_state.states_integers
    pancake_len = len(pancake_lst_int)
    sum_h = 0
    i = 0
    #searches for the first pancake that is not located well from the bottom
    while pancake_len-pancake_lst_int[i] == i:
        i += 1
        if i == pancake_len:
            return 0
    for j in range(i,pancake_len):
        sum_h += pancake_lst_int[j]
    return sum_h


def advanced_heuristic(_pancake_state):
    pancake_lst_int = _pancake_state.states_integers
    pancake_len = len(pancake_lst_int)
    sum_h = pancake_len
    for i in range(1, len(pancake_lst_int)):
        if abs(pancake_lst_int[i] - pancake_lst_int[i - 1]) != 1:
            sum_h += pancake_lst_int[i] + pancake_lst_int[i - 1]
            if i == 1:
                sum_h += pancake_lst_int[i - 1]
    return sum_h