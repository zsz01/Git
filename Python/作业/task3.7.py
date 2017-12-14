def qsort(array,low,high):
    l = low
    h = high
    if low >= high:
        return
    p = array[low]
    while low < high:
        while low < high and array[high] >= p:
            high -= 1
        array[low]=array[high]
        while low < high and array[low] <= p:
            low += 1
        array[high]=array[low]
    array[low]=p
    qsort(array,l,low - 1)
    qsort(array,low + 1,h)

if __name__=="__main__":
    array=[49,38,65,97,76,13,27]
    print(array)
    qsort(array,0,len(array)-1)
    print(array)
