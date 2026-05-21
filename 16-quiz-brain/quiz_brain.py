class QuizBrain():
    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("You got it right!")
            self.score += 1
        else:
            print("That's Wrong.!")
            print(f"The correct answer was {correct_answer.capitalize()}")

    def next_question(self):
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {self.question_list[self.question_number-1].text}. (True/False)?: ").lower()
        correct_answer = self.question_list[self.question_number -1].answer.lower()
        self.check_answer(user_answer,correct_answer)
        print(f"Your current score is {self.score}/{self.question_number}")
        print('\n')

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def completion(self):
        print("You've completed the quiz!!!")
        print(f"Your final score was {self.score}/{len(self.question_list)}")
