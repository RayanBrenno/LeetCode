def sortByBits(arr):
    
    sorted_arr = sorted(arr, key=lambda x: (bin(x).count('1'), x))
    return sorted_arr

    '''
    for x in range(len(arr)-1):
        for y in range(len(arr)-1):
            if (arr[y]>arr[y+1] and bin(arr[y]).count('1') == bin(arr[y+1]).count('1')) or bin(arr[y]).count('1') > bin(arr[y+1]).count('1'):
                arr[y], arr[y + 1] = arr[y + 1], arr[y]

    return arr
    '''


arr = [0,1,2,3,4,5,6,7,8]
print(sortByBits(arr))
