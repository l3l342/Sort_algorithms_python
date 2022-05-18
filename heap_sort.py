def left_child(p):
        return 2 * p + 1

def right_child(p):
        return 2 * p + 2

def swap(list,i,j):
        #Vertauscht das i-te mit dem j-ten Element einer Liste
        temp = list[i]
        list[i] = list[j]
        list[j] = temp
        return list

def repair(list,root,last):
        #Repariert Heap Struktur, falls nötig!
        max = root
        
        left = left_child(root)
        if left <= last and list[max] < list[left]:
                #Fall 1: left child exists and is larger
                max = left
        
        right = right_child(root)
        if right <= last and list[max] < list[right]:
                #Fall 2: right child exists and is larger
                max = right
        
        if max != root:
                #heap property is violated
                swap(list,root,max)
                repair(list,max,last)
        return list

def make_heap(list):
        last = len(list) - 1
        for i in range(last + 1):
                heap = repair(list,last-i,last)
                print(heap)
        return heap

def heap_sort(list):
        make_heap(list)
        last = len(list) - 1
        for i in range(last):
                swap(list,0,last-i)
                repair(list,0,last-i-1)
        return list
        

#list=[25,1,19,7,100,36,17,2,3]
list=[3,9,-3.5,7,1,3]
make_heap(list)
#print(list)
#print(heap_sort(list))
