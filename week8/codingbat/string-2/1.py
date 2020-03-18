# Return True if the string "cat" and "dog" appear the same number of times in the given string.
# cat_dog('catdog') → True
# cat_dog('catcat') → False
# cat_dog('1cat1cadodog') → True


def cat_dog(str):
    c_cat = 0
    c_dog = 0
    for i in range(len(str)-1):
        if str[i:i + 3] == 'cat':
            c_cat += 1
        if str[i:i + 3] == 'dog':
            c_dog += 1
    return c_cat == c_dog


print(cat_dog('1cat1cadodog'))

