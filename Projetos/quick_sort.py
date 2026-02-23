def quick_sort(array):
    if len(array) < 1:
        return array

    pivot = array[0]
    lessPivot = []
    morePivot = []
    equalPivot = []    
    for i in range(len(array)):
        if array[i] == pivot:
            equalPivot.append(array[i])
        elif array[i] > pivot:
            morePivot.append(array[i]) 
        else:
            lessPivot.append(array[i])
    return quick_sort(lessPivot) +  equalPivot + quick_sort(morePivot)