#quicksort algorithmus ~ Sebastion, Beni, Paulus

unsorted_list = [4,6,8,15,4,3, -6, 84,5]

def quicksort(List):
    if len(List) <= 1:
        return List   

    pivot = List.pop()
    
    shorter_List = []
    greater_List = []

    for elem in List:
        if elem < pivot:
            shorter_List.append(elem)
        else:
            greater_List.append(elem)
    return quicksort(shorter_List) + [pivot] + quicksort(greater_List)


a = quicksort(unsorted_list)
print(a)
