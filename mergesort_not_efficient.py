#by Ben und Paul

def merge(List1, List2):
    Zeiger1 = 0
    Zeiger2 = 0
    fertige_Liste = []

    for i in range(len(List1)+len(List2)):
        if Zeiger1 > len(List1)-1:
            return fertige_Liste + List2[Zeiger2:]
        elif Zeiger2 > len(List2)-1:  
            return fertige_Liste + List1[Zeiger1:]
            
        elif List1[Zeiger1] < List2[Zeiger2]:
            fertige_Liste.append(List1[Zeiger1])
            Zeiger1 += 1
        else:
            fertige_Liste.append(List2[Zeiger2])
            Zeiger2 += 1
        


def sort(Liste):
    short = []
    leng = []

    short = Liste[:len(Liste)//2]
    leng = Liste[len(Liste)//2:]

    if len(Liste) <= 2:
        return merge(short, leng)

    return merge(sort(short),sort(leng))
    

Liste = [4,8,5,345,34,1,-54,3]

print(sort(Liste))



