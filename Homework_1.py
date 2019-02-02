Exercise 1
print("Learning Python for Data Science")

Exercise 2
first_name = "Yevgeniya"  # Exercise 2 - Python code
last_name = "Terlyuk"
print(first_name)
print(last_name)

2b
class_name = "Python for Data Science"
which_day = "Saturdays"
Num_days = "eight"
Class_timings = "9 am to noon"
sentence = "{} is on {} {} {}".format(class_name, Num_days, which_day, Class_timings)
print(sentence)

Exercise 3
first_name = "Yevgeniya" 
last_name = "Terlyuk"
two_first = first_name[0:2]
two_last = last_name[-2::]
print(two_first)
print(two_last)

Exercise 4
new_list = [1, "A", 2, "B", 3, "C"]
print(new_list[0:5:2])
print(new_list[1:6:2])

Exercise 5
state_name = "California" 
if state_name == "California":
    print("Golden State")
if state_name == "Texas":
    print("Lone Star State")
else:
    print("Not Golden State or Lone Star State")
    
Exercise 6
???

Exercise 7
def square_and_sum(a,b):
    c = a**2 + b**2
    return c
square_and_sum(2,3)

def add_strings(str1,str2):
    sentence = str1 + " " + str2 + "!!!"
    return sentence
add_strings("Hello","Wourld")

Exercise 8
for x in range(10,0,-1):
    print(x)
    
Exercise 9
states_list = ["California", "Texas", "Arizona"]
states_list.append("Florida")
states_list.remove("Texas")
states_list.sort()
print(states_list)
states_list.sort(reverse=True)
print(states_list)

Exercise 10

Albert_Einstein = "Life is like riding a bicycle. To keep your balance you must keep moving"
print(Albert_Einstein.count("you"))
print(Albert_Einstein.count("ing"))
print(Albert_Einstein.count("life"))

Exercise 11
states_1 = ["Washington","Oregon","California"]
states_2 = ["Texas","Arizona","New Mexico","Nevada"]
states_3 = ["Florida","Georgia","Alabama","Louisiana"]
states_123 = states_1 + states_2 + states_3
states_123.sort()
print(states_123)
