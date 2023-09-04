# function def
def hello(name):
  print("Hi! " + name)

# lambda function
hello = lambda name: print("Hi! " + name)

# control flow

## if
def grading(score):
  # doctring 
  """
  this function ruturn grade for a student in UK
  """
  if score >= 70:
    return "Distinction"
  elif score >= 60:
    return "Merit"
  elif score >= 50:
    return "Passed"
  else:
    return "Failed"

grading(65)

## for loop
nums = [1, 2, 3, 4, 5]
nums*2  # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

new_nums = [] # empty list

for num in nums:
  new_nums.append(num*2)

print(new_nums)  

# list comprehension
y = [num*2 for num in nums]

print(y)

## program to check odd/ even numbers
for num in nums:
  if num % 2 == 0:
    print(f"{num} is even")
  else:
    print(f"{num} is odd")

## while loop
count = 0

while count < 5:
  print("hello")
  # this line is very important
  count = count + 1 # or count += 1

## shortcut to update varibles
x = 1
x += 1
x
x -= 1
x
x *= 5
x
x /= 2
x

# get in put from a user
def animal_guessing():
  set_animal = "hippo"
  answers = []
  while True:
    guess = input("Guessing the animal: ")
    answers.append(guess)
    if guess == set_animal:
      print("Hooray! correct answer.")
      print(f"Logs: {answers}")
      break
    elif guess == "quit":
      print("See you next time.")
      break
    else:
      print("Nope! please try again.")

animal_guessing()      

# OOP: Object Oriented Programming

## Dog class
class Dog:
  def __init__(self, name, age, breed):
    self.name = name
    self.age = age
    self.breed = breed
    
  ## methods (functions)
  def sleep(self):
    print("I'm sleeping now.")
    
  def get_older(self, year):
    self.age += year

## create a new instance
dog1 = Dog("john", 3, "chihuahua")
dog2 = Dog("jane", 2,"golden")

dog1.name
dog1.sleep()
dog1.get_older(3)
dog1.age

## string method
text = "I am happy"

text.split(" ")

"Hello WORLD".lower()

## Superclass
class Person:
  def __init__(self, name):
    self.name = name

class Employee(Person):
  def __init__(self, name, company, position):
    super().__init__(name)
    ### Superclass entend feature from base class
    self.name = name
    self.company = company
    self.position = position
  def greeting(self):
    print(f"Hi my name is {self.name} and I work for {self.company}")

ps1 = Person("Pu")
ps2 = Employee("John", "Google", "Data Aanlyst")
ps2.greeting()

# try except box
try:
  print(abcd)
except ZeroDivisionError:
  print("Cannot divide by zero")
except NameError:
  print("Variable not found in our environment")
else:
  print("OK")
finally:
  print("End!")
## Then, the following code can be run.

# try except SyntaxErroy
try:
  eval('print(1+5 ')
except:
  print("Syntax error")

# magin command in python

## print working directory
!pwd

## list file in folder
!ls  

## print
!echo hello world

## concatenate
!cat penguins.csv

# native way to read csv
import csv

file = open("penguins.csv", mode = 'r')
data = csv.reader(file)

for row in data:
  print(row)

# close file
file.close()

# pandas
import pandas
pandas.read_csv("penguins.csv")

# context manager (with)
## use to open data file and auto close file

### import csv
from csv import reader
result = []

with open("penguins.csv", "r") as file:
  data = reader(file) ### csv.reader
  for row in data:
    result.append(row)
  
result

## write mode
import csv

header = ["id", "course", "students"]
body_data = [
  [1, "data science", 30],
  [2, "marketing", 28],
  [3, "power BI", 35]
]

with open("course.csv", "w") as file:
  writer = csv.writer(file)
  writer.writerow(header)
  writer.writerows(body_data)

!cat course.csv

## csv
import json

with open("data.json", "r") as file:
  data = json.load(file)
  
print(data, type(data))

## dict => json
import json # .load(), .dump()
book = {
  "name": "Testing_name",
  "year": 1998,
  "author": "Bam",
  "favorite": True
}

with open("book.json", "w") as file:
  json.dump(book, file)
  print("Create file successfully!")

!cat book.json  

# API: Appllication Programming Interface

## request-response
import requests
import time

url = "http://swapi.dev/api/people/1"

resp = requests.get(url)

## if success, OK = 200
resp.status_code

## see information
resp.text
resp.json()
resp.json()["name"]


## loop for 5 charactes
range(5)
list(range(5))

characters = []

for i in range(5):
  url = f"http://swapi.dev/api/people/{i+1}"
  resp = requests.get(url)
  
  if resp.status_code == 200:
    json_data = resp.json()
    characters.append(
      (resp.json()["name"],
      resp.json()["height"])
    )
  else:
    characters.append("error")
  
  # break a second before next request
  time.sleep(1)

print(characters)

# Web Scraping
## !pip install gazpacho
!pip list
## pi = package manager in Python
import gazpacho

## import function
from gazpacho import Soup

url = "https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc"
html = requests.get(url)
html.text
imdb = Soup(html.text)
imdb
imdb.find("title")
imdb.find("h1")
titles = imdb.find("h3", {"class": "lister-item-header"})
titles[0].strip() # remove everything that isn't pure text.

clean_titles = []

for title in titles:
  clean_titles.append(title.strip())
  
clean_titles

## list comprehension
clean_titles = [title.strip() for title in titles]
clean_titles

## get rating from the website
## div: ratings-imdb-rating
ratings = imdb.find("div", {"class": "ratings-imdb-rating"})
clean_ratings = [float(rating.strip()) for rating in ratings]
clean_ratings

# join table
import pandas as pd

movie_database = pd.DataFrame(data = {
  "title": clean_titles,
  "rating": clean_ratings
})

movie_database.head(5)

# numerical python
import numpy as np

nums = [1,2,3,4,5]
nums = np.array(nums) # convert from list to array
type(nums)
nums + 5
nums.mean()
#nums.median() # this will get error
np.median(nums)

np.arange(10) # range
np.arange(10) + 1

np.linspace(0, 10, num = 5)

## 2d array
n2 = np.array([
  [1,2],
  [3,4]
])

print(n2, type(n2))

## matrix * matrix
## .dot notation
m1 = np.array([[1,2],[3,4]])
m2 = np.array([[4,2],[1,1]])
np.dot(m1, m2)

# import pandas
import pandas as pd
