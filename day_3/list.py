list1=[12,13,14,15]
list2=[57,23,12,0]
list=list1+list2
print(list)
list.append(99)
print(list.sort()) #asending
print(list) 
print(list.sort(reverse=True)) #desending
print(list)
list.reverse()
print(list)
print(type(list))
list.remove(99)
print(list)