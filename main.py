from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for entry in question_data:
    new_question = Question(entry["text"], entry["answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
# generating new quizbrain object WITH the questions we are using here
# QuizBrain is a model into which we can plug any kind of questions

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz.")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")