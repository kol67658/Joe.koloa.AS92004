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




# Title
print('Uproar')
print('By Joe Koloa')

import time
import os
import time


# Variables Output
str_playername = ""
questions = ['q1', 'q2', 'q3' , 'q4' , 'q5' , 'q6']
points = 0
play_again = True 
answer = ''
correct = (f"Correct, you now have {points + 1} points")
incorrect = (f" Wrong, you now have 0/6 points") 
results = (f'You got {points} out of 6 questions')

time.sleep(1)

print(f'Hello player, welcome to my quiz about the 2023 NZ featured film "Uproar", please answer 0 out of 6 questions') 
print(f'IF you made a mistake, that is ok, as long you answer each questions. But each questions has a timer, ending in 20 seconds')
print(f'To start, please enter your username')

print('What is your name?')
str_playername = input()

print('Welcome {}, please press enter'.format(str_playername))


print('Question 1')
print('Who is the Director of the film? \n a. Hamish Bennet \n b. Cliff Curtis \n c. Peter Jackson \n d. Jemaine Clement ')
answer = input('')
if answer == 'Hamish Bennet' or 'a':
    points =+ 1
    print(correct)

else:
    print(incorrect)


print('Questions 2')
print('Who play as John Waaka?\nHint: He appeared in the Hunter of the wilderpeople \n a. Julian Dennison \n b. Uli Latukefu \n c. KJ APA \n d. Martinson Henderson' )

answer = answer.lower()

if answer == 'Julian Dennison' or 'a':
    print(correct)
    points =+ 1
else:
    print(incorrect)
    
    

print('Question 3')
print('Who played as Jamie Waaka , john brother? hint: He played as alemein in boy \n a. Daniel logan \n b. James Rolleston \n c. Kaimana')


answer = answer.lower()

if answer == 'James Rolleston' or 'b':
   print(correct)
   points += 1

else:
    print(incorrect)
  
   
print('Question 4')
print('Which clip of the film is based on one of the true event in 1981? \n a. Springbok tour protest \n b. Queen Street riot \n  c. Montego Bay \n d. All black won the world cup ')
answer = answer.lower()

if answer == 'Springbok tour protest' or 'a':
   print(correct)
   points += 1
else:
    print(incorrect)
    
    
  
print('Question 5')
print('Julian Dennison is an experienced rugby player in real life, True or False')

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
else:
    print(incorrect)
    
print("You got" + int(points) + " out of 6 questions correct!")


# VARIABLES OUTPUT
str_playeranswer = ''
bool_questionLoop = True
str_playername = input()


print('Hello player, Welcome to my quiz about a 2023 NZ featured film, "Uproar" , please answer one of the following questions')
print('To start, please enter your name')
str_playername = input('')
list_quizquestions = ["Who is the Director of the film? \n a. Hamish Bennet \n b. Cliff Curtis \n c. Peter Jackson \n d. Jemaine Clement ", 
                    "Who play as John Waaka?\nHint: He appeared in the Hunter of the wilderpeople \n a. KJ APA  \n b. Uli Latukefu \n c. Julian dennison \n d. Martinson Henderson", 
                    "Where is it filmed? \n a. Auckland \n b. Dunedin \n c. Christchurch \n d. Wellington ",
                    "Which clip of the film is based on one of the true event ocurred in 1981? \n a. All blacks won the world cup \n b. Queen Street riot \n  c. Montego Bay \n d. Springboks tour",
                    "Julian Dennison is an experienced rugby player in real life, True or False?"
                    ""]
list_quizanswer = ['a', 'c', 'b', 'd' 'True', '100']

MAX_SCORE = len(list_quizquestions)

for i in range(len(list_quizquestions)):
    print(MAX_SCORE)
    bool_questionLoop = True
    print(list_quizquestions[i])
    while bool_questionLoop == True:
       
        str_playeranswer = input(f'What is the correct answer? a,b,c,d')
        if str_playeranswer == list_quizanswer[i]:
            print(" You are Very Correct indeed!")
            bool_questionLoop = False
        else:
            print("Whoops, that is Incorrect womp womp")
            bool_questionLoop = False

# VARIABLES OUTPUT
str_playeranswer = ''
bool_questionLoop = True
str_playername = input('')
points = 0
list_points = (f'You got {points} points out of six questions, Well done!')

print('Hello player, Welcome to my quiz of a 2023 NZ featured film, Uproar, \n A rugbv filled movie presenting with coming of age, codes of masculinity and racism, and rugby as an obliterating cultural force in provincial New Zealand.') 
print('please answer one of the following questions')
print('To start, please enter your name')
str_playername = input('')
print(f'Welcome {str_playername} , please press enter')
enter = input('')
list_quizquestions = ["Who is the Director of the film? \n a. Paul Middleditch \n b. Cliff Curtis \n c. Peter Jackson \n d. Jemaine Clement ", 
                    "Who play as John Waaka?\nHint: He appeared in the Hunter of the wilderpeople \n a. KJ APA  \n b. Uli Latukefu \n c. Julian dennison \n d. Martinson Henderson", 
                    "Where is it filmed? \n a. Auckland \n b. Dunedin \n c. Christchurch \n d. Wellington ",
                    "Which clip of the film is based on one of the true event ocurred in 1981? \n a. All blacks won the world cup \n b. Queen Street riot \n  c. Montego Bay \n d. Springboks tour",
                    "Is Julian Dennison is an experienced rugby player in real life? \n a. Yes \n b. No \n c. Maybe \n d. IDK",
                    "How can you describe the film? \n a. Funny \n .b Poignant \n .c scary \n .d Emotional"]
list_quizanswer = ['a', 'c', 'b', 'd', 'a', 'd']
MAX_SCORE = len(list_quizquestions)

# CREATE LIST TO ADD POINTS AT EACH QUESTIONS IF CORRECT
list_points = ['1+', '2+', '3+', '4+', '5+', '6+']


for i in range(len(list_quizquestions)):
    print(MAX_SCORE)
    bool_questionLoop = True
    print(list_quizquestions[i])
    while bool_questionLoop == True:
       
        str_playeranswer = input(f'What is the correct answer? a,b,c,d')
        if str_playeranswer == list_quizanswer[i]:
            points =+1
            points =+2
            points =+3
            points =+4
            points =+5
            points =+6
            print(" You are Very Correct indeed!")
            bool_questionLoop = False
        else:
            print("Whoops, that is Incorrect womp womp")
            bool_questionLoop = False

print(f'You got' + str(points) +'  out of 6 questions, Well done!')     
    
