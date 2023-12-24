import random


class QuizBrain():
    def __init__(self, question_bank):
        self.frontier = []
        self.player_score = 0
        self.question_list = question_bank
        self.question_number = 1
        self.select = ''

    def next_question(self):
        while len(self.frontier) != len(self.question_list):
            self.select = random.choice(range(12))
            if self.select not in self.frontier:
                self.frontier.append(self.select)
                print(f'Q.{self.question_number}: {self.question_list[self.select].q_text}')
                player_answer = input('True or False\n').lower()
                main_answer = self.question_list[self.select].q_answer
                self.check_answer(player_answer, main_answer)
                self.question_number += 1

    def check_answer(self,player_answer,main_answer):
        print(main_answer, player_answer)
        if player_answer == main_answer.lower():
            self.player_score += 1
            print(f'You are right\nPlayer Score {self.player_score}/{self.question_number}')
        else:
            print(f'You are wrong :( \nPlayer Score {self.player_score}/{self.question_number}')
