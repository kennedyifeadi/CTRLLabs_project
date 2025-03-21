print('''Welcome to the quiz!
Answer the following questions to test your knowledge.''')

print('But, first of all, what is your name?')

name = input('Type your name here: ')

print(f'Ok {name}, let\'s get started!')

print('Question 1: What is the capital of France?')

points = 0

while points==0:
    answer1 = input('Type your answer here: ')
    if answer1.lower() != 'paris':
        print('Wrong answer, try again.')
    else:
        points += 10
        print(f'Congrats, you chose the right answer, you now have {points} points.')
        break

print('Question 2: What is a goup of crows called?')

while points==10:
    answer2 = input('Type your answer here: ')
    if answer2.lower() != 'murder':
        print('Wrong answer, try again.')
    else:
        points += 10
        print(f'Congrats, you chose the right answer, you now have {points} points.')
        break

print('Question 3: What is the only even prime number?')

while points==20:
    answer3 = input("Type your answer here:")
    if answer3.lower() != "2" or answer3.lower()!='two':
        points += 10
        print(f'Congrats, you chose the right answer, you now have {points} points.')
        break
    elif answer3.lower() != "2" and answer3.lower()!='two':
        print('Wrong answer, try again.')
    

print('Great, now you\'ve reached the end of the quiz. See you later.')