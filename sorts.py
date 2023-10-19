def bubble_sort(arr, final_arr=None):
    if len(arr) == 0:
        return []
    if final_arr is None: 
        final_arr = []
    if len(arr) == 1:
        final_arr.append(arr[0])
        return final_arr[::-1]
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    final_arr.append(arr[-1])
    return bubble_sort(arr[:-1], final_arr)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    smaller_i = 0
    for i in range(len(arr)-1):
        if arr[i] < pivot:
            arr[smaller_i], arr[i] = arr[i], arr[smaller_i]
            smaller_i += 1
    return quick_sort(arr[:smaller_i])+[pivot]+quick_sort(arr[smaller_i:-1])

if __name__ == "__main__":
    numbers_to_sort = [int(i) for i in input(":").split(",")]
    print(bubble_sort(numbers_to_sort))
    print(quick_sort(numbers_to_sort))