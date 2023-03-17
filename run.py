# Movie Trivia Game

import getch
import os
import random
import time
import gspread
import datetime
import sys
from google.oauth2.service_account import Credentials
from termcolor import colored

# import path to the questions_data
sys.path.insert(0, './assets/code')

from questions_data import easy_questions, medium_questions, hard_questions, question_points

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
                    break
                

def intro_screen():
    '''
    Intro into the game
    '''

    clear_screen()
    with open('./assets/text_files/titles.txt', 'r') as titles:
        for line in titles:
            slow_print(line, 'yellow')
    
    key_press()
    
    how_to_play()

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


def how_to_play():
    '''
    Prints out the info about how to play the game
    '''
    clear_screen()
    with open('./assets/text_files/how_to_play.txt', 'r') as f:
        display_text = f.read()
    slow_print(f'{" " * 25}How to play this Game\n', 'red')
    slow_print(display_text, 'yellow')
    key_press()

    return

def titles(slow_printing=True):
    '''
    Print Quiz game title header
    '''
    with open('./assets/text_files/titles_heading.txt', 'r') as f:
        heading = f.read()
    
    clear_screen()
    if slow_printing == True:
        slow_print(heading, 'blue')
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

def slow_print(text, color='white', seconds=0.005):
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
        name = input(colored('\n\nInsert name - min 3 characters long, not only numbers and no spaces: \n\n', 'yellow')).strip()
        if name.isdigit():
            slow_print('Invalid name. Cannot be only a number!', 'red')
            name = ''
        elif len(name) < 3:
            slow_print('Invalid name length. Remember, at least 3 letters!', 'red')
            name = ''
        elif ' ' in name:
            slow_print('Invalid name. No spaces!', 'red')
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
    threshold = question_points[(question_num-1)//5*5] if question_num > 5 else 0
    slow_print(f'{50*" "}Points guaranteed: {"{:,}".format(threshold)}', 'red') 
    slow_print(f'\n{name}, this is a question for {"{:,}".format(question_points[question_num])} points:', 'yellow')
    slow_print(f'\n\n {question}')
    print('\n\nChoose a correct answer: \n')
    choice_list = ['a', 'b', 'c', 'd']
    for i in range(4):
        slow_print(f'{choice_list[i]}. {answers[i]}\n')
    while True:
        answer = input(colored('\nChoose a, b, c, d or q: \n', 'yellow')).lower().strip()
        if answer == 'q':
            return question_points[question_num-1] if question_num > 1 else 0
        elif answer not in choice_list:
            print("\n Invalid input! Please, do as you're told! \n")
            continue
        else:
            break
    if choice_list.index(answer) != correct_answer_index:
        slow_print(f'{name}, that is not the right answer. Right answer is {choice_list[correct_answer_index]}.\n', 'red')
        time.sleep(1)
        return threshold
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
    slow_print(f'\n\n\n{name}, you are on the way to be awarded a million useless points!!! WOOHOOOOO!\n', 'green')
    key_press()
    for i in range(15):
        response = display_question(
            name,
            i+1,
            quiz.questions[i]['question'],
            quiz.questions[i]['answers'],
            quiz.questions[i]['correct_answer_index'])
        if response in [item for item in question_points.values()]+[0]:
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
        slow_print('\nNo scores available\n', 'blue')
    else:
        # sorting the list of lists was adapted from https://www.geeksforgeeks.org/python-sort-list-according-second-element-sublist/
        data = sorted(data[1:], key = lambda x: int(x[1]), reverse=True)
        print()
        for index in range(len(data)):
            username = data[index][0]
            score = "{:,}".format(int(data[index][1]))
            date = data[index][2]
            slow_print(f'{username}{(10-len(username))*" "}|{(13-len(score))*" "}{score} | {date}\n', 'yellow')
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

def details_win(case, name):
    '''
    Returns the appropriate elements for the details
    to display by quiz_end function
    '''
    
    if case == 1:
        with open('./assets/text_files/millionaire.txt', 'r') as congrats:
            message = congrats.read()
        
        shout = (colored(f'\n\n{name} is our newest millionaire!!!', 'red'))
        disclaimer = ('\nYeeeeeaaaaah! Just a reminder - you have received a million points.\n')
        return message, shout, disclaimer
    elif case == 2:
        with open('./assets/text_files/good_try.txt', 'r') as congrats:
            message = congrats.read()
        shout = (colored(f'\n\n{name}, you are not far away from the goal!', 'green'))
        disclaimer = '\nYou entered into the high scores...\n'
        return message, shout, disclaimer
    elif case == 3:
        with open('./assets/text_files/good_start.txt', 'r') as congrats:
            message = congrats.read()
        shout = colored(f'\n\n{name}, that was a first step!', 'blue')
        disclaimer = '\nYou entered into the high scores...\n'
        return message, shout, disclaimer
    else:
        with open('./assets/text_files/what.txt', 'r') as congrats:
            message = congrats.read()
        shout = (colored(f'\n{name}, are you tired?', 'red'))
        disclaimer = '\nRelax and try again...\n'
        return message, shout, disclaimer


def quiz_end(name, score):
    '''
    Displays the winning(or losing) screen
    '''

    clear_screen()
    titles(False)
    if score == 1000000:
        message, shout, disclaimer = details_win(1, name)
    elif score >= 32000:
        message, shout, disclaimer = details_win(2, name)
    elif score > 0:
        message, shout, disclaimer = details_win(3, name)
    else:
        message, shout, disclaimer = details_win(4, name)

    print(f'GAME OVER with total of {"{:,}".format(score)}.')
    slow_print(message, 'yellow')
    print(shout)
    slow_print(disclaimer)
    key_press()

def win(result):
        name = result[0]
        if result[1] == 'win':
            score = 1000000
            save_highscores(name, score)
            quiz_end(name, score)
        elif result[1] == 0:
            quiz_end(name, 0)
        else:
            score = result[1]
            save_highscores(name, score)
            quiz_end(name, score)
        
        return

def end_game():
    '''
    Game's exit screen
    '''

    clear_screen()
    titles()
    slow_print(f'\n\n\n{" "*25}Thanks for playing!\n\n', 'yellow')
    key_press()


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
            menu_choice = input(colored('Choose a, b, c, or d: \n\n', 'yellow')).lower().strip()
            if menu_choice == 'a':
                result = quiz_start()
                win(result)
            elif menu_choice == 'b':
                display_highscores()
            elif menu_choice == 'c':
                how_to_play()
            elif menu_choice == 'd':
                end_game()
                return
            else:
                print('\nWrong input!\n')
                menu_choice = ''

if __name__ == "__main__":
    main()
