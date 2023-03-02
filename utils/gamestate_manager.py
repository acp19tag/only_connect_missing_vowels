import os
import time
import random
from collections import Counter

def ask_question(question, answer):
    
    start_time = time.time()
    key_press = input(f'Clue:\t{question:<40} Press ENTER to buzz in!')
        
    total_time = time.time() - start_time

    print(f'The answer was {answer}.')
    user_response = input("Were you correct? < 'y' for yes, 'n' for no, 'a' for abstain > ")

    return user_response, total_time

def parse_response(user_response):
    if user_response in {'y'}:
        return 'correct'
    elif user_response in {'n'}:
        return 'incorrect'
    elif user_response in {'a'}:
        return 'abstain'
    else:
        print(f'Invalid response: {user_response}.')
        
def score_response(user_response):
    parsed_response = parse_response(user_response)
    if parsed_response == 'correct':
        return 1
    elif parsed_response == 'incorrect':
        return -1
    return 0

def clear_screen():
    """
    Clears the terminal of stuff.
    'clear' is for Mac/Linux, 'cls' is for Windows.
    """
    
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


class GameStateManager:
    
    def __init__(self, QuestionHandler) -> None:
        
        self.QuestionHandler = QuestionHandler
        
    def start_game(self):
        
        clear_screen()
        
        print('Welcome to the Only Connect game!\n')
        
        n_rounds = input('How many rounds would you like to play? Choose "e" for endless mode. ')
                
        if n_rounds == 'e':
            n_rounds = len(self.QuestionHandler.questionsets)
                
        self.play_game(int(n_rounds))
                
                
    def play_game(self, n_rounds):
        
        random_question_set_ids = random.sample(self.QuestionHandler.get_id_set(), n_rounds)

        recorded_times = []
        correct_times = []
        round_response_list = []
        round_score_list = []

        for round_index, random_question_set_id in enumerate(random_question_set_ids):
            
            clear_screen()
            
            print('*'*20)
            print(f'Round {round_index+1} of {n_rounds}')
            print('*'*20)
            print()

            _ = input(f'The category is: {self.QuestionHandler.questionsets[random_question_set_id].set_label}. Press ENTER to start the round. ')

            for question, answer in self.QuestionHandler.questionsets[random_question_set_id].get_qa_tuples():

                response, time_taken = ask_question(question, answer)

                round_response_list.append(response)
                recorded_times.append(time_taken)

                if parse_response(response) == 'correct':
                    correct_times.append(time_taken)

            round_score = sum(score_response(response) for response in round_response_list)
            
            # uhh probably not necessary but maybe just in case
            # let's normalise scores for a 4 question round
            if len(round_response_list) != 4:
                round_score = round_score * 4 / len(round_response_list)
                
            round_score_list.append(round_score)

        response_Counter = Counter([parse_response(response) for response in round_response_list])

        clear_screen()
        print('*'*20)
        print('Round Summary:')
        print('*'*20)
        print()
        print(f"Completed rounds: {round_index + 1}")
        print(f"Number correct: {response_Counter['correct']} ({response_Counter['correct']/sum(response_Counter.values()):.2%})")
        print(f"Number incorrect: {response_Counter['incorrect']} ({response_Counter['incorrect']/sum(response_Counter.values()):.2%})")
        print(f"Number abstained: {response_Counter['abstain']} ({response_Counter['abstain']/sum(response_Counter.values()):.2%})")
        print(f'Average time: {sum(recorded_times)/len(recorded_times):.2f} seconds')
        print(f'Average time (correct only): {sum(correct_times)/len(correct_times):.2f} seconds')
        print(f'Average round score: {sum(round_score_list)/len(round_score_list):.2f} points')
        print()