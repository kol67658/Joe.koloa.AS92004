# Title
print('Uproar')
print('By Joe Koloa')

import time
import os
import time


# Variables Output
questions = ['q1', 'q2', 'q3' , 'q4' , 'q5' , 'q6']
points = 0
play_again = True
answer = ''


time.sleep(1)

print('Hello there, welcome to my quiz of the 2023 NZ featured film "Uproar", please answer 0 out of 6 questions') 
print('IF you made a mistake, that is ok, as long you answer each questions.')
print('To start, please enter your username')

print('What is your name?')
name = input()

print('Welcome {}, please press enter'.format(name))

print('Question 1')
print('Who is the Director of the film? \n a. Hamish Bennet \n b. Cliff Curtis \n c. Peter Jackson \n d. Jemaine Clement ')
answer = answer.lower()
if answer == 'hamish bennet' or 'a':
   print('That is Correct, good job!')
   print('You got 1/6 points')
   points += 1
else:
 print('Womp Womp, the correct answer is Hamish bennet, 0/6 ')
    
print('Questions 2')
print('Who play as John Waaka?\nHint: He appeared in the Hunter of the wilderpeople')

answer = answer.lower()

if answer == 'Julian Dennison':
    print('Wow! correct again! 2/6')
    points += 1
else:
    print('Whoops, the correct answer is Julian Dennison 0/6')
    

print('Question 3')
print('Who played as Jamie Waaka , john brother? hint: He played as alemein in boy')

answer = answer.lower()

if answer == 'James Rolleston':
   print('That is correct, 3/6')
   points += 1

else:
    print('Uh oh, the correct answer is James Rolleston, 0/6')
    
print('Question 4')
print('Which clip of the film is based on one of the most controversial and violent event in 1981? \n a. Springbok tour protest \n b. Queen Street riot \n  c. Montego Bay \n d. All black won the world cup ')
answer = answer.lower()

if answer == 'Springbok tour protest':
   print('Wow you are on fire! 4/6')
   points += 1
else:
    print('Womp Womp again, 0/6 ')
    
    
    
print('Question 5')
print('Is Julian Dennison an experienced rugby player? True or False?')

answer = answer.lower()

bool_ans1 = True
bool_ans2 = False

if answer == 'True':
    print('Wow, one more to go , 5/6')
    points += 1
else:
    print('OOf, sorry wrong again, 0/6')

print('Question 6')
print('What do you think of my game, rating out of 100? 20, 60, 75, or 100?')

answer = input()

if answer == '20' or '60' or '75' or '100':
    print('Wow, Thank you so much for playing my game , 6/6')
    points += 1
    print('Here is your prize')
    print('You have received $200,000,000')
    
print("You got" + int(points) + " questions correct!")








