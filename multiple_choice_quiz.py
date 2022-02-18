'''
This is example of multiple choice quiz
'''
from Questions import questions

question_prompt = [
    "what color are Mangoes?\n(a) Red\n(b) Yellow\n(c) black\n(d) Green\n\n",
    "what color are Rambutan?\n(a) Purple\n(b) Orange\n(c) Blue\n(d) Red\n\n",
    "waht color are Mangoesteen?\n(a) Red\n(b) Purple\n(c) Green\n(d) Blue\n\n"
]

Questions = [
    questions(question_prompt[0], "b"),
    questions(question_prompt[1], "d"),
    questions(question_prompt[2], "b")
]

def the_quiz(Questions):
    score = 0
    for questions in Questions:
        answer = input(questions.prompt)
        if answer == questions.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")