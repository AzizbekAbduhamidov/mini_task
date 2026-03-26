def filtr(sonlar):
 yangi=[]
 for son in sonlar: 
  if son>0:
   yangi.append(son)
 return yangi
if __name__=="__main__":
    print(filtr([3,-5,4,-8]))