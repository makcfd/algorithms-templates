
def is_substring(s, t):
    if s == "":
        return True
    if s[0] in t:
        return is_substring(s[1:], t[t.index(s[0])+1:])
    else:
        return False


source = "abc"
target = "ahbgdcu"

print(is_substring(source, target))
