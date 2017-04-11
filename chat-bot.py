import random
from time import sleep as offset 
print ("Hi, My name is Vell, I'm your Virtual Assistant")
offset(2)
print ("Initializing...")
offset(3)
print ("I'll be asking you some questions, let's begin with the Test!")
offset(2)
name = raw_input("So, Tell me your name:")
offset(2)
if name.isalpha():
    if name <= str(5):
        print ("Now I know that your name is " + name + ", You know? You have a short name...")
        offset(2)
    elif name >= str(5):
        print ("Now I know that your name is " + name + ", You know? You have a large name...")
        offset(2)
else:
    print "Oops! I didn't quite get that..."
    offset(2)
    print "Maybe you wrote a number instead of a letter..."
age = raw_input("How old are you?")
offset(2)
print ("Hmm...")
offset(2)
if age <= str(18):
    print ("You don't look like you're " + age + ", Psst... I'm older than you!")
    offset(2)
else:
    print ("You don't look like you're " + age + ", Psst... You're older than me!")
    offset(2)
phrase_1 = "That's the color of happiness"
phrase_2 = "That's the prettiest color"
phrase_3 = "I like that one too"
phrases = phrase_1, phrase_2, phrase_3
color_choice = raw_input("What is your favorite color?")
offset(2)
color_1 = ['green', 'yellow']
color_2 = ['red', 'black']
color_3 = ['blue', 'white']
if color_choice == random.choice(color_1):
    print random.choice(phrases)
    offset(2)
elif color_choice == random.choice(color_2):
    print random.choice(phrases)
    offset(2)
elif color_choice == random.choice(color_3):
    print random.choice(phrases)
    offset(2)
while_user = raw_input("Hey, Would you like to stay for a while?")
ans_no_1 = "Ahh, ok..."
ans_no_2 = "Well, it's your choice..."
ans_no_3 = "Ok. Fair enough"
answers_no = ans_no_1, ans_no_2, ans_no_3
if while_user == 'No' or 'no':
    print random.choice(answers_no)
    offset(2)
elif 'Yes' or 'yes' in while_user:
    print "Ok."
    offset(2)

print "Well, I'll be here if you need me..."
offset(2)
print "Ask me anything you want..."
query = raw_input()



    

    
