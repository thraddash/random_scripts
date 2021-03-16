#!/usr/bin/env python

test_list = [1, 2, 3, 4, 5]
remove_list = [2, 4, 5]

## list comprehension
res = [i for i in test_list if i not in remove_list]

print(f"test_list = {test_list}")
print(f"remove_list = {remove_list}\n")
print(f"list comprehension: {res}")

## lambda ##
res2 = list(filter(lambda i: i not in remove_list, test_list))
print(f"lambda: {res2}")

## Set, creating a new filtered list of all the elements that are not present in the remove element list
set1 = set(test_list)
set2 = set(remove_list)
res3 = list(set1 - set2)
print(f"set: {res3}")

## remove() method takes a single element as an arguement and removes it from the list
# if the element doesn't exit, it throws a ValueError ##
for i in remove_list:
    try:
        test_list.remove(i)
    except ValueError:
        pass
print(f"remove: {test_list}")

#
