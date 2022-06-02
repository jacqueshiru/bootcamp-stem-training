fruits=["apple", "orange", "banana"]
fruits.append("cherry")
print(fruits)

fruits.remove("cherry")


fruits=["apple", "orange", "banana"]
fruits_2=["cherry", "tomato", "pineapple"]
fruits_3=[fruits+fruits_2]
print(fruits_3)
fruits.extend(fruits_2)
print(fruits)
fruits_2.clear()
print(fruits_2)


fruits_4=("apple", "orange", "something")
print(fruits_4)
print(fruits_4[1])




#tupples cannot  be added or removed
new_lists= list(fruits_4)
new_lists.append("tomato")
fruits_4=tuple(new_lists)

#sets don't allow duplicate value


my_list=[2,4,1,7,8,10,12]
for elem in my_list:
    print(elem)


other_list=[]
my_list=[2,4,1,7,8,10,12]
for elem in my_list:
    other_list.append(elem)
print(other_list)



my_list=[2,4,1,7,8,10,12]
other_list=[elem for elem in my_list]
print(other_list)


my_list=[2,4,1,7,8,10,12]
other_list=[elem for elem in my_list]


for elem inp my_list:
    if elem % 2==0:
        other_list.append(elem)
print(other_list)
