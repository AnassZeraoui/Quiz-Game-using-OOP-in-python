from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

Question_Bank = []
for i in question_data:
    question_text = i["question"]
    question_answer = i["correct_answer"]
    new_question = Question(question_text,question_answer)
    Question_Bank.append(new_question)

quiz = QuizBrain(Question_Bank)
while quiz.still_has_question():
    quiz.next_question()

print("Excellent , You've completed the Quiz Game")
print(f"Your score is {quiz.score}/{len(Question_Bank)}")
