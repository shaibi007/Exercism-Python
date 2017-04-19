import re
def is_isogram(text):
    m = re.findall('[a-z]',text.lower())
    my_set = set(m)
    if len(my_set) == len(m):
        return True
    else:
        return False

print(is_isogram('Helo Wrd'))
