# Movie Trivia Game

import getch
import os
import random
import time
import gspread
import datetime
from google.oauth2.service_account import Credentials
from questions import easy_questions, medium_questions, hard_questions, question_points
from termcolor import colored

MENU = [
    'a. Start Quiz Game',
    'b. High Scores',
    'c. How to Play Instructions',
    'd. Quit the Game'
]

SCOPE = [
  'https://www.googleapis.com/auth/spreadsheets',
  'https://www.googleapis.com/auth/drive.file',
  'https://www.googleapis.com/auth/drive'
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('millionaire_highscores')
high_scores = SHEET.worksheet('high_scores')

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
    print('\nPlease, press a key...')
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

def titles(slow_printing=True):
    '''
    Print Quiz game title header
    '''
    with open('./assets/text_files/titles-heading.txt', 'r') as f:
        heading = f.read()
    
    clear_screen()
    if slow_printing == True:
        slow_print(heading, 'blue', 0.01)
    else:
        print(colored(heading, 'blue'))
    
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
        name = input('\n\nInsert your name: \n')
        if name.isdigit():
            slow_print('Who gave you that name? Please, choose something else!')
            name = ''
    return name


def display_question(name, question_num, question, answers, correct_answer_index):
    '''
    The function displays the question by writing a question order number,
    the question itself and all the answers. It asks for a user to
    select the correct answer and gives the output for the wrong/write
    answer.
    '''
    titles(False)
    treshold = question_points[(question_num-1)//5*5] if question_num > 5 else 0
    slow_print(f'{50*" "}Points guaranteed: {"{:,}".format(treshold)}', 'red') 
    slow_print(f'\n{name}, this is a question for {"{:,}".format(question_points[question_num])} points:', 'yellow')
    slow_print(f'\n\n {question}')
    print('\n\nChoose a correct answer: \n')
    choice_list = ['a', 'b', 'c', 'd']
    for i in range(4):
        slow_print(f'{choice_list[i]}. {answers[i]}\n')
    while True:
        answer = input(colored('\nChoose a, b, c, d or q: \n', 'yellow'))
        if answer.lower() == 'q':
            return question_points[question_num-1] if question_num > 1 else 0
        elif answer.lower() not in choice_list:
            print("\n Invalid input! Please, do as you're told! \n")
            continue
        else:
            break
    if choice_list.index(answer.lower()) != correct_answer_index:
        slow_print(f'{name}, that is not the right answer. Right answer is {choice_list[correct_answer_index]}.\n', 'red')
        time.sleep(1)
        return treshold
    else:
        print(f"{name}, you're good! Well done.")
        time.sleep(1)

def quiz_start():
    '''
    Quiz control function
    '''
    
    quiz = Quiz()
        
    titles()
    name = insert_username()
    slow_print(f'\n\n\n{name}, you are on the way to be awarded a million useless points!!! WOOHOOOOO!', 'green')
    key_press()
    for i in range(15):
        response = display_question(
            name,
            i+1,
            quiz.questions[i]['question'],
            quiz.questions[i]['answers'],
            quiz.questions[i]['correct_answer_index'])
        if response in [0, 1000, 32000]:
            return name, response
        else:
            pass
    
    return name, 'win'

def display_highscores():
    '''
    Displays recorded high scores if there are some from
    the Google Sheets
    '''

    global high_scores

    data = high_scores.get_all_values()

    titles()
    slow_print('\nHIGH SCORES\n', 'red')
    if len(data) == 1:
        slow_print('\nNo scores available\n', 'blue', 0.01)
    else:
        # sorting the list of lists was adapted from https://www.geeksforgeeks.org/python-sort-list-according-second-element-sublist/
        data = sorted(data[1:], key = lambda x: int(x[1]), reverse=True)
        print()
        for index in range(len(data)):
            username = data[index][0]
            score = "{:,}".format(int(data[index][1]))
            date = data[index][2]
            slow_print(f'{username}{(10-len(username))*" "}|{(13-len(score))*" "}{score} | {date}\n', 'yellow', 0.01)
    print('\n')
    key_press()
    return

def save_highscores(username,score):
    '''
    After winning some points in the game, this function saves
    the high score to the Google Sheets
    '''

    global high_scores
    date = datetime.date.today().strftime('%d/%m/%Y')
    new_row = [username, score, date]
    high_scores.append_row(new_row)

def display_win(name, score):
    '''
    Displays the winning screen
    '''

    pass

def main():
    '''
    A main function.
    '''

    intro_screen()
    
    # Menu section
    while True:
        clear_screen()
        titles(False)
        print('\n\n\n')
        for item in MENU:
            print(colored(item+'\n', 'red'))
        
        menu_choice = ''
        while menu_choice == '':
            menu_choice = input(colored('Choose a, b, c, or d: \n\n', 'yellow'))
            if menu_choice.lower() == 'a':
                result = quiz_start()
                win(result)
            elif menu_choice.lower() == 'b':
                display_highscores()
            elif menu_choice.lower() == 'c':
                rules()
            elif menu_choice.lower() == 'd':
                exit()
            else:
                print('\nWrong input!\n')
                menu_choice = ''


def win(result):
        name = result[0]
        if result[1] == 'win':
            score = 1000000
            save_highscores(name, score)
            display_win(name, score)
        elif result[1] == 0:
            display_win(name, 0)
        else:
            score = result[1]
            save_highscores(name, score)
            display_win(name, score)
        
        return

main()
