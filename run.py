# Movie Trivia Game

import getch
import os
import random
import time
from questions import *
from termcolor import colored

class Quiz:
    '''
    A class for the quiz questions
    '''

    def __init__(self):
        self.questions = []
        self.generate_questions()

    def generate_questions(self):
        '''
        generates 15 random questions from the database
        5 for each difficulty level
        '''
        question_control_list = []
        if len(self.questions) != 0:
            self.questions = []
        level = ['easy', 'medium', 'hard']
        for i in range(15):
            while True:
                (selected_question, all_answers, correct_answer_index) = choose_question(level[i//5])

                # Check if the randomly chosen question is already in the list
                if selected_question not in question_control_list:
                    question_control_list.append(selected_question)
                    self.questions.append(
                        {'question': selected_question,
                        'answers': all_answers,
                        'correct_answer_index': correct_answer_index,
                        })
                    print('No!')
                    break
                else:
                    print('Yeah!')

def intro_screen():
    '''
    Intro into the game
    '''

    clear_screen()
    with open('./assets/text_files/titles.txt', 'r') as titles:
        for line in titles:
            slow_print(line, 'yellow', .01)
    
    key_press()
    
    rules()

    return


def key_press():
    print('\n\nPlease, press a key...')
    key = getch.getch()

    return


def clear_screen():
    '''
    Clears the terminal screen
    '''


    # detects if the script is run on MS Windows system
    # and uses the corresponding command
    if os.name == 'nt':
        os.system('cls')

    # for Linux/MacOs different clear command
    else:
        os.system('clear')


def rules():
    '''
    Prints out the info about how to play the game
    '''
    clear_screen()
    slow_print('Just something to have it here', 'blue', 0.01)
    key_press()

    return

def titles():
    '''
    Print Quiz game title header
    '''
    with open('./assets/text_files/titles-heading.txt', 'r') as f:
        heading = f.read()
    
    clear_screen()
    slow_print(heading, 'blue', 0.01)
    
    return


def choose_question(level):
    '''
    Makes a random choice of the questions from the dictionaries
    according to the level given as a parameter.
    The function returnes a tuple 
    (question, answers_list, right_answer_index)
    '''
    if (level == 'easy'):
        question = random.choice(easy_questions)
    elif level == 'medium':
        question = random.choice(medium_questions)
    elif level == 'hard':
        question = random.choice(hard_questions)
    else:
        raise ValueError('Invalid level Value')

    # copy the incorrect answers with a correct one into
    # one list and shuffle it
    answers = question['incorrectAnswers'][:]
    correct_answer = question['correctAnswer']
    answers.append(correct_answer)
    random.shuffle(answers)
    selected_question = question['question']
    return selected_question, answers, answers.index(correct_answer)

def slow_print(text, color='white', seconds=0.001):
    '''
    Slow printing text function with 
    text, color and time in seconds parameters
    '''

    for letter in text:
        print(colored(letter, color), end='', flush=True)
        time.sleep(seconds)


def insert_username():
    '''
    Insert username function
    '''

    name = ''
    while not name:
        name = input('Insert your name: ')
        if name.isdigit():
            slow_print('Who gave you that name? Please, choose something else!')
            name = ''
    return name


def display_question(question_num, question, answers, correct_answer_index):
    '''
    The function displays the question by writing a question order number,
    the question itself and all the answers. It asks for a user to
    select the correct answer and gives the output for the wrong/write
    answer.
    '''
    titles()
    treshold = question_points[(question_num-1)//5*5] if question_num > 6 else 0
    slow_print(f'{50*" "}Points guaranteed: {treshold}', 'red') 
    slow_print(f'Question for {question_points[question_num]}:\n\n {question[:-1]}, \n\n', 'yellow')
    print('\n\nChoose a correct answer: \n')
    choice = ['a', 'b', 'c', 'd']
    for i in range(4):
        slow_print(f'{choice[i]}. {answers[i]}\n')
    while True:
        answer = input('Choose a, b, c, or d: \n')
        if answer.lower() not in choice:
            print("\n Invalid input! Please, do as you're told! \n")
            continue
        else:
            break
    if choice.index(answer.lower()) != correct_answer_index:
        slow_print(f'That is not the right answer. Right answer is {choice[correct_answer_index]}.\n', 'red')
    else:
        print(f"You're good! Well done.")


def quiz_start():
    '''
    Quiz control function
    '''
    
    quiz = Quiz()
        
    titles()
    name = insert_username()
    slow_print(f'\n\n\n{name}, you are on the way to be awarded a million useless points!!! WOOHOOOOO!', 'green')
    slow_print('\n\nPress any key when ready...')
    key_press()
    for i in range(15):
        display_question(
            i+1, quiz.questions[i]['question'],
            quiz.questions[i]['answers'],
            quiz.questions[i]['correct_answer_index'])  

def main():
    '''
    A main function.
    '''

    intro_screen()
    
    # Menu section
    clear_screen()
    # while True:
    #     pass

    quiz_start()

            

main()
