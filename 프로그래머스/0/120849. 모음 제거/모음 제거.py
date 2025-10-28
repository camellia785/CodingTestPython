def solution(my_string):
    mo = ["a", "e", "i", "o", "u"]
    for my in my_string:
        if my in mo:
            my_string = my_string.replace(my, "")
    return my_string