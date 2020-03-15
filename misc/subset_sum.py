# The subset sum is to find subset of elements that are selected from a
# given set whose sum adds up a given number K. Note: no duplicates,
# no non-negatives


def subset_sum(elements, k):

    for i, e in enumerate(elements):
        if e == k:
            return [e]
        elif e < k:
            subset = subset_sum(elements[i + 1:], k - e)
            if subset:
                return [e] + subset


print(subset_sum([15, 22, 14, 26, 32, 9, 16, 8], 53))
