def orta(sonlar):
    if not sonlar:
        return 0
    return sum(sonlar)/len(sonlar)
print(orta([3,5,7,4,2,8]))
print(orta([]))