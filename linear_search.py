def search(arr, x):
    n = len(arr)

    for i in range(0, n):
        if arr[i] == x:
            return i
        return -1

if __name__ == "__main__":
        arr = [2,3,4,5,70,80,100,20,25,15]
        x = 2

        res = search(arr, x)
        if (res == -1):
            print("Element is not present in array")
        else:
            print("Element is present at index", res)