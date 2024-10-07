questions = ("What is a correct syntax to output 'Hello World' in Python?",
            "Which one is NOT a legal variable name?",
            "What is the correct file extension for Python files?",
            "What is the correct syntax to output the type of a variable or object in Python?",
            "Which method can be used to remove any whitespace from both the beginning and the end of a string?")

options = (("A. p('Hello World')","B. echo('Hello World');","C. echo 'Hello World'","D. print('Hello World')"),
        ("A. _myvar","B. my-var","C. Myvar","D. my_var"),
        ("A. .pt","B. .puth","C. .py","D. .pyt"),
        ("A. print(typeof x)","B. print(typeOf(x))","C. print(type(x))","D. print(typeof(x))"),
        ("A. trim()","B. ptrim()","C. strip()","D. len()"))
answers = ("D","C","C","C","D")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("--------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRRECT!")
        print(f"{answers[question_num]} is te correct answer")
    question_num +=1

print("--------------------------")
print("         RESULT           ")
print("--------------------------")

print("answers:",end="")
for answer in answers:
    print(answer,end="")
print()

print("guesses:",end="")
for guess in guesses:
    print(guess,end="")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")