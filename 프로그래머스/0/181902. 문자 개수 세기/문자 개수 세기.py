import string 

def solution(my_string):
    alphabet = string.ascii_uppercase + string.ascii_lowercase
    return [my_string.count(ch) for ch in alphabet]