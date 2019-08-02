def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]


    print("Sorted Array: ")
    for i in range(len(arr)):
        print("{0}".format(arr[i]))


arr = [45,93,23,1,34]
bubble_sort(arr)
