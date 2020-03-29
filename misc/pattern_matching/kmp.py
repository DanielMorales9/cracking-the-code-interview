# Knuth Morris Pratt Algorith for pattern matching
# searching a substring in the text


def kmp(text, sub):
    j = 0  # length of the previous longest prefix suffix
    n = len(sub)
    lps = [0] * n
    i = 1

    # the loop calculates lps[i] for i = 1
    while i < n:
        if sub[i] == sub[j]:
            j += 1
            lps[i] = j
            i += 1
        elif j != 0:
            j = lps[j - 1]
        else:
            lps[i] = 0
            i += 1

    i = j = 0
    while i < len(text) and j < n:
        var_1, var_2 = text[i], sub[j]
        if var_1 == var_2:
            i += 1
            j += 1
        elif j > 0:
            j = lps[j-1]
        else:
            i += 1

    return j == len(sub)


haystack = "abcxabcdabxabcdabcdabcy"
needle = "abcdabcy"

print(kmp(haystack, needle))
