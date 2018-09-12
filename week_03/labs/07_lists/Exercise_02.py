'''
Given the two lists below, find the elements that are the same
and put them in a new list.
Put the elements that are different in another list.

Print both.

'''

list_one = [0, 4, 6, 18, 25, 42, 100]
list_two = [1, 4, 9, 24, 42, 88, 99, 100]

same_list = list()
diff_list = list()

for x in list_one:
    if x in list_two:
        same_list += x
    else:
        diff_list += x
