def quick_sort(list):
        #sorted_list wird die sortierte Version von list (bleibt unverändert)
        if len(list) > 1:
                smaller = []
                greater = []
                for i in range(1,len(list)):
                        if list[i] <= list[0]:
                                smaller.append(list[i])
                        else:
                                greater.append(list[i])
                sorted_smaller = quick_sort(smaller)
                sorted_greater = quick_sort(greater)
                return sorted_smaller + [list[0]] + sorted_greater                                         
        else:
                return list

def swap(list,i,j):
        #Vertauscht das i-te mit dem j-ten Element einer Liste
        temp = list[i]
        list[i] = list[j]
        list[j] = temp
        return list

def partition(list,anfang,ende):
#Teilt list in ein zwei Teile (links, die Elemente, die kleiner sind als das Pivotelement, rechts die Elemente, die größergleich sind)
        grenze = anfang 
        for index in range(anfang + 1,ende):
                if list[index] < list[anfang]:
                        grenze += 1
                        swap(list,grenze,index)
        swap(list,anfang,grenze)#Partition Ende
        return grenze

def qsort(list,anfang,ende):
        #list wird umsortiert
        if anfang < ende:
                grenze = partition(list,anfang,ende)
                list = qsort(list,anfang,grenze - 1)
                list = qsort(list,grenze + 1,ende)
                return list
        return list

                
                

list=[6,3,8,54,3,8,34,7]

print(qsort(list,0,len(list)))