#Problem : https://www.hackerrank.com/challenges/swap-case/problem

def swap_case(s):
    new_str = ""
    for s in s:
        if s.islower():
            new_str += s.upper()
        else:
            new_str += s.lower()
    return new_str