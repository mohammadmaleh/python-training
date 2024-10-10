value = 1
# while value <= 10:
#     print(value)
#     if value == 5:
#         break
#     value += 1
# print("done")


value2 = 1
while value2 <= 10:
    value2 += 1
    if value2 == 5:
        continue
    print(value2)
else:
    print(" value now is equal to  " + str(value2))

names = ["mohammad", "gray", "khalid"]
for name in names:
    print(name) # mohammad gray khalid

for name in names:
    if name == "gray":
        break
    print(name)  # mohammad

for name in names:
    if name == "gray":
        continue
    print(name)  # mohammad gray

for x in range(4):
    print(x)  # 0 1 2 3

for x in range(1, 4):
    print(x)  # 1 2 3

for name in range(0, 100, 10):
    print(name)  # 0 10 20 30 40 50 60 70 80 90

for name in range(100, 0, -10):
    print(name)  # 100 90 80 70 60 50 40 30 20 10

# nested loops
names = ["mohammad", "gray", "khalid"]
actions = ["eat", "sleep", "code"]
for name in names:
    for action in actions:
        print(name + " " + action) # mohammad eat mohammad sleep mohammad code gray eat gray sleep gray code khalid eat khalid sleep khalid code 

for action in actions: 
    for name in names:
        print(name + " " + action) #  mohammad eat gray eat khalid eat mohammad sleep mohammad sleep gray sleep khalid sleep mohammad code mohammad code