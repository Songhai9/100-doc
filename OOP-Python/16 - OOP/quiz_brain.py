class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def check_answer(self, answer):
        correct_answer = self.question_list[self.question_number].answer
        if answer.lower() ==  correct_answer.lower():
            print('You are right')
            self.score += 1
        else:
            print('You are wrong')
        print(f'The correct answer was {correct_answer}')
        print(f'Your current score is {self.score}/{self.question_number + 1}')

    def next_question(self):
        user_answer = input(
            f"Q.{self.question_number + 1} {self.question_list[self.question_number].text} : "
        )
        self.check_answer(user_answer)
        self.question_number += 1
        

    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        return False
