def permutation(list1, list2):
     if len(list1) != len(list2):
          return False
     list1.sort()
     list2.sort()
     if list1 == list2:
        print("they are permutation")
     else: 
         print("they arent")


list1 = [1,2,43,5,6,8,2,3]
list2 = [3,2,1,43,6,8,2,2]

permutation(list1,list2)

