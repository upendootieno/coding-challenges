#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Approach:
    # Loop through each item of the list
    # And update counters based on the
    # value of the current item
    positive = 0
    negative = 0
    zero = 0

    for x in arr:
        if x < 0:
            zero += 1
        elif x > 0:
            positive += 1
        else:
            negative += 1

    total = positive + negative + zero
    positive_ratio = positive/total
    negative_ratio = negative/total
    zero_ratio = zero/total

    print("%.6f" % positive_ratio)
    print("%.6f" % negative_ratio)
    print("%.6f" % zero_ratio)


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(
        map(
            int, input().rstrip().split()
        )
    )

    plusMinus(arr)
