class QuizBrain:

    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1 
        user_answer = input(f"Q.{self.question_number}: {current_question.text}. (True/False)?: ").lower()
        self.check_answer(user_answer, current_question.answer)
    
    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            print("Right answer!")
            self.score +=1
        else:
            print("You're wrong, mate.")
        
        print(f"The correct answer was {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}.")
        print("\n"*2)
    
    def end_of_game(self):
        print("You have completed the game!")
        print(f"Your final score is: {self.score}/{len(self.question_list)}")