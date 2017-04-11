import random 
print ("Hi, My name is Vell, I'm your Virtual Assistent")
print ("I'll be asking you some questions, let's begin with the Test!")
name = raw_input("So, Tell me your name:")
if name <= str(5):
    print ("Now I know that your name is " + name + ", You know? You have a short name")
elif name >= str(5):
    print ("Now I know that your name is " + name + ", You know? You have a large name")
age = raw_input("How old are you?")
if age <= str(18):
    print ("You don't look like you're " + age + ", Psst... I'm older than you!")
else:
    print ("You don't look like you're " + age + ", Psst... You're older than me!")
