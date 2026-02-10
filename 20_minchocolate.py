#given an array of positive integers where each value represents the number of chocolates in a packet, each packet can have a variable number of chocolates there are m students the task is to distribute chocolate packets among students such that 1) each student gets exactly one packet 2) the d/f b/w maximum number of chocolate given to a student and minimum num of chocolate given to a student is minimum return that minimum possible d/f

def min_chocolate_difference(arr, m):
    if m == 0 or len(arr) < m:
        return -1

    arr.sort()
    min_diff = float('inf')

    for i in range(len(arr) - m + 1):
        min_diff = min(min_diff, arr[i + m - 1] - arr[i])

    return min_diff

print(min_chocolate_difference([3, 4, 1, 9, 56, 7, 9, 12], 5))