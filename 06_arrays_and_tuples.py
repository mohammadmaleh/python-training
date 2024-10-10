users = ["Dave", "Sarah", "Malcolm"]
data = ["Dave", 42, True]
emptyList = []
print("Dave" in users)  # True
print(users[0])  # Dave
print(users[1])  # Sarah
print(users[-2])  # Sarah
print(users.index("Sarah"))  # 1
print(users[0:2])  # ['Dave', 'Sarah']
print(users[1:])  # ['Sarah', 'Malcolm']
print(len(data))  # 3


users.append("Hannah")  # add to the end
print(users)  # ['Dave', 'Sarah', 'Malcolm', 'Hannah']

users += ["John"]  # add to the end
print(users)  # ['Dave', 'Sarah', 'Malcolm', 'Hannah', 'John']

users.extend(["Hannah", "John"])  # add to the end
print(users)  # ['Dave', 'Sarah', 'Malcolm', 'Hannah', 'John', 'Hannah', 'John']

users.insert(0, "John")  # add to the beginning
users[2:2] = ["Hannah", "John"]  # add at the range  (2, 2)

users[1:3] = ["Sarah", "Malcolm"]  # replace at the range

users.remove("Hannah")  # remove the first occurrence
users.pop()  # remove the last element
# users.clear()  # remove all elements
del users[0]  # remove by index

del data  # remove data
# print(data)  # error because data is not defined

users.sort()  # sort
print(users)  # ['Dave', 'Hannah', 'John', 'Malcolm', 'Sarah']

users.reverse()  # reverse
print(users)  # ['Sarah', 'Malcolm', 'John', 'Hannah', 'Dave']

print("here")
users[1:2] = ["ayham"]
users.sort()  # when sorting the list, the elements that are strings will be sorted alphabetically but the small letter will come last
print(users)


users.sort(
    key=str.lower
)  # sorts the list alphabetically but  the small letter will be sorted properly


nums = [3, 41, 12, 9, 74, 15]
nums.sort()  #  [3, 9, 12, 15, 41, 74]
nums.sort(reverse=True)
print(nums)  # [74, 41, 15, 12, 9, 3]


print(sorted(nums))  # global sorting,  doesn't affect the original list


nums_copy = nums.copy()  # copy
another_nums_copy = list(nums)  # copy
another_nums_copy2 = nums[:]  # copy


print(type(nums))  # <class 'list'>


# tuples

users = ("Dave", "Sarah", "Malcolm")
another_tuples = (1, 2, 3)
print(users)  # ('Dave', 'Sarah', 'Malcolm')
print(type(users))  # <class 'tuple'>


new_users = list(users)  # convert tuple to list
new_users.append("Hannah")
print(new_users)  # ['Dave', 'Sarah', 'Malcolm', 'Hannah']
print(users)  # ('Dave', 'Sarah', 'Malcolm')
users = new_users
print(users)  # ['Dave', 'Sarah', 'Malcolm', 'Hannah']


(one, two, *others) = [1, 2, 3, 4, 5]
print(one)  # 1
print(two)  # 2
print(others)  # [3, 4, 5]
