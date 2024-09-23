DEBUG = False

from question_model import Question
from quiz_brain import QuizBrain
from data import question_data


question_bank = []

for question in question_data:
    cleaned_question = question["question"].replace("&quot;","'").replace("&#039;", "'")
    # Instantiate question objects and append them to the question list
    question_bank.append(Question(cleaned_question, question["correct_answer"]))

if DEBUG:
    for question in question_bank:
        print(f"Question: {question.question}\nAnswer: {question.answer}\n")

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.user_score}/{quiz.question_number}.")
