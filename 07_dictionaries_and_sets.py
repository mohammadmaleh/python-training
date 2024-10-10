# Dictionaries
band = {
    "vocals": "Plant",
    "guitar": "Stevie Wonder",
    "drums": "Ritchie Blackmore",
    "bass": "Daron Malakian",
}
band2 = dict(
    vocals="Plant",
    guitar="Stevie Wonder",
    drums="Ritchie Blackmore",
    bass="Daron Malakian",
)
print(
    band
)  # {'vocals': 'Plant', 'guitar': 'Stevie Wonder', 'drums': 'Ritchie Blackmore', 'bass': 'Daron Malakian'}
print(
    band2
)  # {'vocals': 'Plant', 'guitar': 'Stevie Wonder', 'drums': 'Ritchie Blackmore', 'bass': 'Daron Malakian'}

print(type(band))  # <class 'dict'>
print(len(band))  # 5

print(band["vocals"])  # Plant
print(band.get("guitar"))  # Stevie Wonder
print(band.keys())  # dict_keys(['vocals', 'guitar', 'drums', 'bass']
print(
    band.values()
)  # dict_values(['Plant', 'Stevie Wonder', 'Ritchie Blackmore', 'Daron Malakian'])
print(
    band.items()
)  # dict_items([('vocals', 'Plant'), ('guitar', 'Stevie Wonder'), ('drums', 'Ritchie Blackmore'), ('bass', 'Daron Malakian')])


# verify if key exists
print("guitar" in band)  # True
print("guitar" not in band)  # False

# change value
band["vocals"] = "Mick Jagger"
print(
    band
)  # {'vocals': 'Mick Jagger', 'guitar': 'Stevie Wonder', 'drums': 'Ritchie Blackmore', 'bass': 'Daron Malakian'}

# add new key
band["keyboards"] = "Jimi Hendrix"
print(
    band
)  # {'vocals': 'Mick Jagger', 'guitar': 'Stevie Wonder', 'drums': 'Ritchie Blackmore', 'bass': 'Daron Malakian', 'keyboards': 'Jimi Hendrix'}

# remove item
del band["keyboards"]
print(
    band
)  # {'vocals': 'Mick Jagger', 'guitar': 'Stevie Wonder', 'drums': 'Ritchie Blackmore', 'bass': 'Daron Malakian'}
band.pop("bass")  # remove bass

# copy a dictionary
band2 = band  # creates a reference, they both reference the same value in memory
band2 = band.copy()  # creates a copy of the dictionary
band3 = dict(band)  # creates a copy of the dictionary

# nested dictionaries
member1 = {
    "name": "John",
    "instrument": "guitar",
}
member2 = {
    "name": "Sarah",
    "instrument": "bass",
}
band = {
    "members": [member1, member2],
}
print(
    band
)  # {'members': [{'name': 'John', 'instrument': 'guitar'}, {'name': 'Sarah', 'instrument': 'bass'}]}


# sets
nums = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
nums2 = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(nums)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(nums2)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(type(nums))  # <class 'set'>
print(len(nums))  # 10

# it accepts only unique values
nums.add(2)
print(nums)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# True is a deduplicate of 1 and False is a deduplicate of 0
nums = {1, True, False, 0}
print(nums)  # {1, False}

# check if a value is in a set
print(2 in nums)  # True
print(2 not in nums)  # False

# but you cannot refer to an element in a set with an index position or a key

# add a new element to a set 
nums.add(8)

# you can add elements from one set into another
more_nums = {112, 113, 114}
nums.update(more_nums)
print(nums)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 112, 113, 114}

# you can use update with list, tup[l;s and dictionaries
# merge two sets to create new set

one = { 1,2,3}
two = {2,3,4,5}
my_new_set = one.union(two)
print(my_new_set)  # {1, 2, 3, 4, 5}

# keep only the doublicates in the set
my_new_set = one.intersection(two)
print(my_new_set)  # {2, 3}