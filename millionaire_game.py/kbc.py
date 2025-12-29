questions='''\n Q1 What is the capital of India?
\n A. Mumbai
\n B. Delhi
\n C. Kolkata
\n D. Chennai \n''','''\n Q2 Which data type is used to store whole numbers in Python?\n A. float
\n B. str
\n C. int
\n D. bool \n
''','''\n Q3 Which keyword is used to start a loop in Python?\n A. if
\n B. loop
\n C. while
\n D. def \n
''','''\n Q4 What does len() do in Python?\n A. Adds numbers
\n B. Finds length
\n C. Converts to string
\n D. Prints output \n
''','''\n Q5 Which symbol is used for comparison in Python?\n A. =
\n B. ==
\n C. !=
\n D. Both B and C \n
'''

answer="B","C","C","B","D"







prize=0
retry=0

i=0
while(i<5):

        #printing ques and taking input
        
    user_ans=input(questions[i])

    user_ans=user_ans.upper().strip()

    if(user_ans==answer[i]):
        print("Correct answer")
        i=i+1
        prize=prize + 10000
        print(prize)
        retry=0
        continue

    elif(retry<2):
        print("wrong! try again")
        retry=retry + 1
        continue

    elif(retry==2):
        print("You lost! ")
        break

    else:
        print("You Lose!")
        break

print(f"Game ended,you earned rupees {prize}")

    

    
    

  










