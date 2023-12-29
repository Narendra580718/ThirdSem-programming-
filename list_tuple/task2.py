# Perform Following Functions in Collections:
# 1. printing the collection
# 2. printing range selection along with negative indexing
# 3. length checking
# 4. type checking
# 5. counting same values
# 6. insert
# 7. delete
# 8. sorting (ascending and descending)
# 9. reverse
# 10. extending or joining
# 11. allow duplicates or not
# 12. print the collection using constructor

#LIST:

collection = ["all","i","want","is","nothing","more"]

print(collection)
print(collection[1:-2])
print(len(collection))
print(type(collection))

print(collection.count("i"))

collection.insert(4,"Something")
print(collection)
collection.pop(-1)
print(collection)

collection.sort()
print(collection)

collection.sort(reverse=True)
print(collection)

collection.reverse()
print(collection)

collection2=["but","everything"]
collection.extend(collection2)
print(collection)

collection.append("Something")
print(collection)


