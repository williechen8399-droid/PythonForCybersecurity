# example working withLoops
#By


def hi():
    for i in range(8): 
        print("Hello World")
        print(i)


def while_example():
    count = 0
    while count < 6:
        print(f"The count is {count}")
        count = count + 1 
def loop_array():
    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
        print(fruit)
    
            

def nested_loop():
    fruits = ["apple", "banana", "cherry"]
    adj = ["shiny", "big", "tasty"]
    for fruit in fruits:
        for a in adj:
            print(f"{a} {fruit}")
    
def loop_breal():
    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
        print(fruit)
        if fruit == "banana":
            break
print("startign")
hi()
while_example()
loop_array()
print('done')
