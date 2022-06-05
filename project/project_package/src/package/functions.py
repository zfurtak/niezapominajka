import string
import glob
import shutil
import os

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


def save_image(image_path, dst_path):
    shutil.copy2(image_path, dst_path)

