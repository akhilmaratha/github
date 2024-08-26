# using function in python
# def greeting(name):
#     return f"hi,{name}"

# name=input("Who do you want to greet? ")
# print(greeting(name)) 

from greet.english   import greet_in_english as greet_english
from greet.hindi import greet_in_hindi as greet_hindi
print(greet_english("akhil"))
print(greet_hindi("akhil"))