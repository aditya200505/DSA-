def print_sum(arr):
    if len(arr) == 0:
        return
    print(arr, "Sum =", sum(arr))
    print_sum(arr[2:])   
arr = [5, 4, 3, 2, 1]
print_sum(arr)