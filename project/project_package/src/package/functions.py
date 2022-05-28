import string

"""
    check whitespace
    True - no whitespace
    False - length == 0 or there is whitespace
    """
def without_whitespace(text):
    if len(text) == 0:
        return False

    for i in text:
        if i in string.whitespace:
            return False
    return True
