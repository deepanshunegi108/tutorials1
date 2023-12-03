'''lists ordered collection of data items
2.stores multiple values 
3. separated by commaas 
4.are muttable in nature '''

lst1 = [1,2,2,3,5,4,6]
lst2 = ["Red", "Green", "Blue"]
print(lst1)
print(lst2)


'''lists indexes every term in lists consists of a index value 
through which we can make changes in it .'''

colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [0]      [1]     [2]      [3]      [4]
# here o ,1,2,3,4 are all indexes of the lists #


# accesing items in the lists through indexes #
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [0]      [1]     [2]      [3]      [4]
print(colors[2])
print(colors[4])
print(colors[0])


# Negative Indexing:

colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [-5]    [-4]    [-3]     [-2]      [-1]
print(colors[-1])
print(colors[-3])
print(colors[-5])

# Check for item:

colors = ["Red", "Green", "Blue", "Yellow", "Green"]
if "Yellow" in colors:
    print("Yellow is present.")
else:
    print("Yellow is absent.")


colors = ["Red", "Green", "Blue", "Yellow", "Green"]
if "Orange" in colors:
    print("Orange is present.")
else:
    print("Orange is absent.")


#Range of Index:        

animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[3:7])	#using positive indexes
print(animals[-7:-2])	#using negative indexes


# printing till end 
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[4:])	#using positive indexes
print(animals[-4:])	#using negative indexes


animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[:6])	#using positive indexes
print(animals[:-3])	#using negative indexes


# printing alternate values 
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[::2])		#using positive indexes
print(animals[-8:-1:2])	#using negative indexes

# Add List Items
#There are three methods to add items to list: append(), insert() and extend()

#append():
#This method appends items to the end of the existing list.

#Example:

colors = ["voilet", "indigo", "blue"]
colors.append("green")
print(colors)


#insert():
# This method inserts an item at the given index. User has to specify index and the item to be inserted within the insert() method.

# Example:

colors = ["voilet", "indigo", "blue"]
#           [0]        [1]      [2]

colors.insert(1, "green")   #inserts item at index 1
# updated list: colors = ["voilet", "green", "indigo", "blue"]
#       indexs              [0]       [1]       [2]      [3]

print(colors)


# #insert():
# This method inserts an item at the given index. User has to specify index and the item to be inserted within the insert() method.

# Example:
colors = ["voilet", "indigo", "blue"]
#           [0]        [1]      [2]

colors.insert(1, "green")   #inserts item at index 1
# updated list: colors = ["voilet", "green", "indigo", "blue"]
#       indexs              [0]       [1]       [2]      [3]

print(colors)




# extend():
# This method adds an entire list or any other collection datatype (set, tuple, dictionary) to the existing list.

# Example 1:

#add a list to a list
colors = ["voilet", "indigo", "blue"]
rainbow = ["green", "yellow", "orange", "red"]
colors.extend(rainbow)
print(colors)


#add a tuple to a list
cars = ["Hyundai", "Tata", "Mahindra"]
cars2 = ("Mercedes", "Volkswagen", "BMW")
cars.extend(cars2)
print(cars)

#add a set to a list
cars = ["Hyundai", "Tata", "Mahindra"]
cars2 = {"Mercedes", "Volkswagen", "BMW"}
cars.extend(cars2)
print(cars)

#add a dictionary to a list
students = ["Sakshi", "Aaditya", "Ritika"]
students2 = {"Yash":18, "Devika":19, "Soham":19}    #only add keys, does not add values
students.extend(students2)
print(students)



# concatenate two lists:
# you can simply concatenate two list to join two lists.

# Example:

colors = ["voilet", "indigo", "blue", "green"]
colors2 = ["yellow", "orange", "red"]
print(colors + colors2)


# Remove List Items
# There are various methods to remove items from the list: pop(), remove(), del(), clear()

 

# pop():
# This method removes the last item of the list if no index is provided. If an index is provided, then it removes item at that specified index.

# Example 1:

colors = ["Red", "Green", "Blue", "Yellow", "Green"]
colors.pop()        #removes the last item of the list
print(colors)

colors = ["Red", "Green", "Blue", "Yellow", "Green"]
colors.pop(1)       #removes item at index 1
print(colors)


# remove():
# This method removes specific item from the list.

# Example:
colors = ["voilet", "indigo", "blue", "green", "yellow"]
colors.remove("blue")
print(colors)


# del:
# del is not a method, rather it is a keyword which deletes item at specific from the list, or deletes the list entirely.

# Example 1:

colors = ["voilet", "indigo", "blue", "green", "yellow"]
del colors[3]
print(colors)


colors = ["voilet", "indigo", "blue", "green", "yellow"]
del colors
print(colors)


# clear():
# This method clears all items in the list and prints an empty list.

# Example:

colors = ["voilet", "indigo", "blue", "green", "yellow"]
colors.clear()
print(colors)

# Change List Items
# Changing items from list is easier, you just have to specify the index where you want to replace the item with existing item.

# Example:

names = ["Harry", "Sarah", "Nadia", "Oleg", "Steve"]
names[2] = "Millie"
print(names)

names = ["Harry", "Sarah", "Nadia", "Oleg", "Steve"]
names[2:4] = ["juan", "Anastasia"]
print(names)

names = ["Harry", "Sarah", "Nadia", "Oleg", "Steve"]
names[1:4] = ["juan", "Anastasia"]
print(names)


names = ["Harry", "Sarah", "Nadia", "Oleg", "Steve"]
names[2:3] = ["juan", "Anastasia", "Bruno", "Olga", "Rosa"]
print(names)



# List Comprehension
# List comprehensions are used for creating new lists from other iterables like lists, tuples, dictionaries, sets, and even in arrays and strings.

 

# Syntax:

# List = [expression(item) for item in iterable if condition]

# expression: it is the item which is being iterated.

# iterable: it can be list, tuples, dictionaries, sets, and even in arrays and strings.

# condition: condition checks if the item should be added to the new list or not. 

 
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O) 


names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if (len(item) > 4)]
print(namesWith_O)


# List Methods
# We have discussed methods like append(), clear(), extend(), insert(), pop(), remove() before. Now we will learn about some more list methods:

 

# sort(): This method sorts the list in ascending order.
# Example 1:

colors = ["voilet", "indigo", "blue", "green"]
colors.sort()
print(colors)

num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort()
print(num)


#  if you want to print the list in descending order?
# We must give reverse=True as a parameter in the sort method.

# Example:
colors = ["voilet", "indigo", "blue", "green"]
colors.sort(reverse=True)
print(colors)

num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort(reverse=True)
print(num)


# reverse(): This method reverses the order of the list. 
# Example:
colors = ["voilet", "indigo", "blue", "green"]
colors.reverse()
print(colors)

num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.reverse()
print(num)



# index(): This method returns the index of the first occurrence of the list item.
# Example
colors = ["voilet", "green", "indigo", "blue", "green"]
print(colors.index("green"))

num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
print(num.index(3))


# count(): Returns the count of the number of items with the given value.
# Example:
colors = ["voilet", "green", "indigo", "blue", "green"]
print(colors.count("green"))

num = [4,2,5,3,6,1,2,1,3,2,8,9,7]