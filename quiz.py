import random
from colorama import init
from colorama import Fore, Style

print("Welcome to my computer quiz!")

questions = [
    ["What is the most abundant gas in Earth's atmosphere?", "Nitrogen"],
    ["What is the second most abundant gas in Earth's atmosphere?", "Oxygen"],
    ["What is the chemical symbol for gold?", "Au"],
    ["What is the chemical symbol for silver?", "Ag"],
    ["What is the chemical symbol for copper?", "Cu"],
    ["What is the chemical symbol for lead?", "Pb"],
    ["What is the chemical symbol for zinc?", "Zn"],
    ["What is the chemical symbol for iron?", "Fe"],
    ["What is the chemical symbol for sulfur?", "S"],
    ["What is the chemical symbol for carbon?", "C"],
    ["What is the chemical symbol for nitrogen?", "N"],
    ["What is the chemical symbol for oxygen?", "O"],
    ["What is the chemical symbol for chlorine?", "Cl"],
    ["What is the chemical symbol for sodium?", "Na"],
    ["What is the chemical symbol for potassium?", "K"],
    ["What is the chemical symbol for calcium?", "Ca"],
    ["What is the chemical symbol for magnesium?", "Mg"],
    ["What is the chemical symbol for aluminum?", "Al"],
    ["What is the chemical symbol for silicon?", "Si"],
    ["What is the chemical symbol for phosphorus?", "P"],
    ["What is the chemical symbol for chlorine?", "Cl"],
    ["What is the chemical symbol for sulfur?", "S"],
    ["What is the chemical symbol for iodine?", "I"],
    ["What is the chemical symbol for bromine?", "Br"],
    ["What is the chemical symbol for chlorine?", "Cl"],
    ["What is the chemical symbol for fluoride?", "F"],
    ["What is the chemical symbol for mercury?", "Hg"],
    ["What is the chemical symbol for titanium?", "Ti"],
    ["What is the chemical symbol for manganese?", "Mn"],
    ["What is the chemical symbol for chromium?", "Cr"],
    ["What is the chemical symbol for cobalt?", "Co"],
    ["What is the chemical symbol for nickel?", "Ni"],
    ["What is the chemical symbol for copper?", "Cu"],
    ["What is the chemical symbol for zinc?", "Zn"],
    ["What is the chemical symbol for silver?", "Ag"],
    ["What is the chemical symbol for gold?", "Au"],
    ["What is the chemical symbol for platinum?", "Pt"],
    ["What is the chemical symbol for lead?", "Pb"],
    ["What is the chemical symbol for sulfur?", "S"],
    ["What is the chemical symbol for chlorine?", "Cl"],
    ["What is the chemical symbol for oxygen?", "O"],
    ["What is the chemical symbol for nitrogen?", "N"],
    ["What is the chemical symbol for carbon?", "C"]
    ]


score = 0
used_questions = []

def quiz_fun():
    global score
    global used_questions
    random_question = random.choice(questions)
    while random_question in used_questions:
        random_question = random.choice(questions)
    used_questions.append(random_question)
    print(Fore.BLUE + Style.BRIGHT + random_question[0])
    answer = input(Fore.GREEN + "Answer: ")
    if answer.lower() == random_question[1].lower():
        print(Fore.GREEN + "Yes, that's correct.")
        score += 1
    elif answer.lower() == "exit":
        print(Fore.GREEN + "Thank you for playing! Your score was", score, "points.")
        quit()
    else:
        print(Fore.RED + Style.BRIGHT + "No, that's not correct. The correct answer is ", random_question[1])
        return

playing = input(Fore.YELLOW + "Do you want to play? (Yes/No) ")
if playing.lower() != "yes":
    quit()
else:
    rounds = int(input(Fore.YELLOW + "How many rounds do you want to play? "))
    for i in range(rounds):
        quiz_fun()
    print(Fore.GREEN + "Thank you for playing! Your score was", score, "points.")
