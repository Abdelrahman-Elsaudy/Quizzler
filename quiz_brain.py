from data import data, AMOUNT


class QuizBrain:
    def __init__(self, questions_data):
        self.data = questions_data
        self.score = 0
        self.number = 0
        self.text = self.data[self.number]["text"]
        self.answer = self.data[self.number]["correct_answer"]

    def still_has_questions(self):
        return self.number < AMOUNT

    def next_question(self):
        self.number += 1
        if self.number < AMOUNT - 1:
            self.text = self.data[self.number]["text"]
            self.answer = self.data[self.number]["correct_answer"]

    def check_answer(self, user_answer):
        if user_answer.lower() == self.answer.lower():
            self.score += 1
            return True
        else:
            return False


quiz = QuizBrain(data)
