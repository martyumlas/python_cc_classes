#list

my_list = [char for char in 'hello']
my_list2 = [num for num in range(0, 100)]
my_list3 = [num*2 for num in range(0, 100)]
my_list4 = [num**2 for num in range(0, 100) if num % 2 == 0]

# print(my_list2)
# print(my_list)
# print(my_list4)

#set
my_set = {num**2 for num in range(0, 100) if num % 2 == 0}

# print(my_set)
# print({1,1,2,2,})
#dictionary
simple_dict = {
    'a':1,
    'b':2
}
my_dict = {key:value**2 for key, value in simple_dict.items()}

# print(my_dict)

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']


duplicates_set = set()

# Create a list to store duplicates
duplicates = [x for x in some_list if some_list.count(x) > 1 and x not in duplicates_set and not duplicates_set.add(x)]

duplicates2 = set([x for x in some_list if some_list.count(x) > 1])

print(duplicates2)





