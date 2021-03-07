import string


def ispangram(str1, alp=string.ascii_lowercase):
    alset = set(alp)
    return alset <= set(str1.lower())


print(ispangram('The quick brown fox jumps over the lazy dog'))