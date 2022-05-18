def merge_sort(list):
        if len(list) <= 1:
                return list
        else:
                half = len(list) // 2
                return merge(merge_sort(list[0:half]),merge_sort(list[half:len(list)]))

def merge(a,b):
        c = [None] * (len(a) + len(b))
        l = 0
        r = 0
        while l + r < len(c):
                if l < len(a) and (r >= len(b) or a[l] <= b[r]):
                        c[l+r] = a[l]
                        l = l + 1
                else:
                        c[l+r] = b[r]
                        r = r + 1
        return c

list=[6,3,8,54,3,8,34,7]

print(merge_sort(list)) 
