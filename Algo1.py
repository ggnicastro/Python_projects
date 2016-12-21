def merge_sort(A):

    if len(A) <= 1:

        return 0, A

    middle = len(A)/2

    left_inversions, left = merge_sort(A[:middle])

    right_inversions, right = merge_sort(A[middle:])

    merge_inversions, merged = merge(left, right)

    inversions = left_inversions + right_inversions + merge_inversions

    return inversions, merged


def merge(left, right):

    result = []

    i, j, inversions = 0, 0, 0

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:

            inversions += j

            result.append(left[i])

            i += 1

        else:

            result.append(right[j])

            j += 1

    inversions += j*(len(left)-i)

    result += left[i:]

    result += right[j:]

    return inversions, result


re = open("./tex.txt", "r").read().split("\n")

total = []

for line in re:
    if len(line) >2:
        total.append(line)
r = total[:]
c = merge_sort(total)
a = [3,2,1]
d = merge_sort(a)