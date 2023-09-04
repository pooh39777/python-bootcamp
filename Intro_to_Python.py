print(2-1)

#string

my_name = "Pu"
my_uni = 'Kasetsart'
long_string = """first line
second line
third line"""

print(my_name, my_uni, long_string)

#fstring template
my_age = 25

text = f"my name is {my_name}, and I am {my_age} years old."
print(text)

#function designed for string (string methods)
type(text)

text.upper()
"Hello World".lower()

text.count("a") #count number of a in text
text.count("old")

text2 = text.replace('name', 'nickname')

print(text)
print(text2)

#list

shopping_list = ['egg', 'milk', 'bread']
print(shopping_list)
print(shopping_list[1])
print(shopping_list[0:2]) #up to 2, but not include 2
print(shopping_list[-1]) #count index from right

#list method = append
shopping_list.append('orange juce')
print(shopping_list)

#list method = insert
shopping_list.insert(0, "grape") #0 is index where to insert new value.

#list method .pop() to remove last item
shopping_list.pop()
print(shopping_list)

#remove specific item
shopping_list.pop(2)
shopping_list.remove('egg')

#add two lists together
item1 = ['a', 'b', 'c']
item2 = ['d', 'e']
full_item = item1 + item2
full_item

#sort items in list
shopping_list.sort()
shopping_list
full_item.sort(reverse = True)
full_item

len(shopping_list) #length

#dictionary key-value pair
student = {
  "id": 1,
  "name": "Mary",
  "movies": ["Spider Man", "Thor", "Iron Man 3"]
}
#key is immutable, dict is mutable

student
type(student)

student['name']
student['movies'][1]
student['movies'][3]
student['test'] #if not find, get error
#or
student.get('movies')
student.get('test') #if not find, not error

#add new key
student['city'] = 'London'
student

#update value
student['city'] = 'Paris'
student

#remove key-value
del student['city']
student

#user-define function
def hello():
  print("Hello!")

hello()

def hello2(username):
  print("Hello! " + username)

hello2("name") 
hello2() #This will be error.

#add default argument
def hello2(username = "default"):
  print("Hello! " + username)
  
hello2() #Now, it's fine.

def my_sum(val1, val2):
  return val1 + val2
  
my_sum(5, 2)

#OOP: Object-oriented programming
class Dog:
  name = "John"
  age = 5
  color = "Brown"
  breed = "French Bulldog"
  
  #fuction (Dog method)
  def sitting(self):
    print("I am sitting now!")
  
  def hungry(self, food_name):
    print(f"I am hungry, I need {food_name}!")

my_dog = Dog()
type(my_dog)

my_dog.age
my_dog.sitting()
my_dog.hungry("mango")

#string + string
## string * number

"blackpink" + " in your area!"
"blackpink" * 3

#function that return multiple values
def demo():
  name1 = input("Pick a name: ")
  name2 = input("Pick a name: ")
  return name1, name2 #tuple

new_name = demo() #notice that tuple is within ( and )
new_name.index("John") #find index of searching word
new_name.count("John")

#tuple unpacking
friend1, friend2 = demo() #number of varibles must = varibles in function
friend1
friend2

#if there are unuse value, we can use _
friend3, _ = demo()

#set {unique set}
fruits = {"apple", "orange", "banana", "banana"}
fruits #don't have duplicate value
uniq_fruit = set(fruits)
len(uniq_fruit)
