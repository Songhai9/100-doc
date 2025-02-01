from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = [Question(q["text"], q["answer"]) for q in question_data]

quizbrain = QuizBrain(question_list=question_bank)

while quizbrain.still_has_question():
    quizbrain.next_question()

print(quizbrain.score)