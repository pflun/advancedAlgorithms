# This function returns median of ar1[] and ar2[].
# Assumptions in this function:
# Both ar1[] and ar2[] are sorted arrays
# Both have n elements
def getMedian(ar1, ar2, n):
    i = 0  # Current index of i/p list ar1[]
    j = 0  # Current index of i/p list ar2[]
    m1 = -1
    m2 = -1

    # Since there are 2n elements, median
    # will be average of elements at index
    # n-1 and n in the array obtained after
    # merging ar1 and ar2
    count = 0
    while count < n + 1:
        count += 1

        # Below is to handle case where all
        # elements of ar1[] are smaller than
        # smallest(or first) element of ar2[]
        if i == n:
            m1 = m2
            m2 = ar2[0]
            break

        # Below is to handle case where all
        # elements of ar2[] are smaller than
        # smallest(or first) element of ar1[]
        elif j == n:
            m1 = m2
            m2 = ar1[0]
            break
        if ar1[i] < ar2[j]:
            m1 = m2  # Store the prev median
            m2 = ar1[i]
            i += 1
        else:
            m1 = m2  # Store the prev median
            m2 = ar2[j]
            j += 1
    return (m1 + m2) / 2