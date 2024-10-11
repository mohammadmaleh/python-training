name = "Mohamad"
count = 1


def another():
    color = "red"
    global count  # if we want to edit the global variable we must define it as global
    count = 2
    print(name, count, color) # mohamad 2 red
    def greeting():
      nonlocal color 
      color = "blue"
      print(name, count, color) # mohamad 2 blue
    greeting()
    print(name, count, color) # mohamad 2 blue


another()
print(count) # 2
