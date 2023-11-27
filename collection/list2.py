# #WAP to print the list 
# #WAP to print the list with different printing methods using list indexing.

# list=input("Enter your number: ")

# print(list)
# print(list[2])

movies=["Rocky Bhai", "Bhalaldev" , "Mahendar Bahubali", "Pushpa", "Parmen", "Doreamon", "dunrik", "RRR"]
# print(type(movies))
# print(movies[3:5])
# print(movies[3:])
# print(movies[:2])
# print(movies[-4:-1])

# movies.append("Chitthi")
# movies.insert(2,"kanchana")

print(movies)

# movies.pop(2)
# print(movies)

# movies.pop() #delets last value
# print(movies)

# movies.remove("Bhalaldev") #delets particular
# print(movies)

# movies.sort() #sorts item alphabetically in order
# print(movies)

# movies[1]="Jawan"
# print(movies)

# movies[2:4]=["Dunki","Spiderman"]
# print (movies)


# print(movies.clear())

list1=["superman", "spiderman", "batman"]
list2=["apple", "banana", "mango"]

list1.extend(list2)
print(list1)

list3=list1+list2
print(list3)

movies.sort(reverse=True)
print(movies)

list4=list1.copy()
print(list4)

movies.sort(key=str.lower) #sort both capital and lower letter together
print(movies)

list4=["misha", "loojman", "dyo"]
list5 = [1,2,3,4,5,6,7,8,9]

for i in list5:
    list4.append(i)
print(list4)

