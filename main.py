string = "HELLO"

def solution(string):
    str_list = []

    for letter in string:
        str_list += letter


    for i in range(round(len(str_list) / 2)):
        temp = str_list[i]
        str_list[i] = str_list[len(str_list) - i - 1]
        str_list[len(str_list) - i - 1] = temp

    return_str: str
    last_letter = None

    for letter in str_list:
        if last_letter:
            return_str = f"{last_letter}{letter}"
            last_letter = f"{last_letter}{letter}"
        else:
            return_str = letter
            last_letter = letter

    return str(f"{return_str}")

print(string, "becomes", solution(string), "when reversed.")