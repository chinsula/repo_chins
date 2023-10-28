# TODO Напишите функцию `is_palindrome`
def is_palindrome(str_):
    str_list = "".join(str_.lower().split())
    str_list1 = str_list[::-1]
    if str_list == str_list1:
        return True
    else:
        return False
print(is_palindrome("А роза упала на лапу Азора"))