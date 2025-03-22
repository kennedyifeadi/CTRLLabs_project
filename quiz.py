print('''Welcome to the CTRL quiz!
Are you ready''')

print('But, first of all, what is your name?')

name = input('Type your name here: ')

print(f'Ok {name}, let\'s get started!')
points = 0
correct = 0

question1 ='Question 1(Maths): What is tan45?'
answer1 = '1'

print(question1)
input1 = input('Type your answer here: ')
if input1.lower() != answer1:
    status1 = False
else:
    points += 10
    correct += 1
    status1 = True

print(f"Great, let's move on")



question2 ='Question 2(Countries): What is the capital of France?'
answer2 = 'paris'

print(question2)
input2 = input('Type your answer here: ')
if input2.lower() != answer2:
    status2 = False
else:
    points += 10
    correct += 1
    status2 = True

print(f"Great, just one more left")



question3 ='Question 3(Biology): What organ is responsible for pumping blood?'
answer3 = 'heart'

print(question3)
input3 = input('Type your answer here: ')
if input3.lower() != answer3:
    status3 = False
else:
    points += 10
    correct += 1
    status3 = True

print(f"Great, just one more left")


    

print("Congrats on reaching the end of the quiz. Here is your summary:")    

print(f''':
\t Question 1: {question1}. 
\t Ans: {answer1}
\t Your input: {input1}
\t Status: {status1}
\n ''')

print(f''':
\t Question 2: {question2}. 
\t Ans: {answer2}
\t Your input: {input2}
\t Status: {status2}
\n ''')

print(f''':
\t Question 3: {question3}. 
\t Ans: {answer3}
\t Your input: {input3}
\t Status: {status3}
\n ''')

print(f''':
\t Total points: {points}. 
\t You got {correct} questions right
\n ''')
