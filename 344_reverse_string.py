# in-place reverse
#
def reverseString(s):
    for i in range(len(s)//2):
        s[i], s[-1 - i] = s[-1 -i], s[i]
