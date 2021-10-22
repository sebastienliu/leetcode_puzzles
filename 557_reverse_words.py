#Input: s = "Let's take LeetCode contest"
#Output: "s'teL ekat edoCteeL tsetnoc"
# Solution 1
def reverseWords(string):
    output = list()
    words = string.split(" ")
    for i in range(len(words)):
        letters = list(words)
        for j in range(len(letters)//2):
            letters[j], letters[-j - 1] = letters[-j - 1], letters[j]
        ostring = "".join(letters)
        output.append(ostring)
    return " ".join(output)

# Solution 2
def reverseWords(self, s: str) -> str:
    output = list()
    s_split = s.split(" ")
    for i in range(len(s_split)):
        letters = s_split[i][::-1]
        output.append(letters)
    return " ".join(output)
