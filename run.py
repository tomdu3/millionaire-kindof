# Movie Trivia Game
from questions import *
import random

# print(easy_questions[0]['question'])
# print(easy_questions[0]['correctAnswer'])
# print(easy_questions[0]['incorrectAnswers'])


def choose_question(level):
    '''
    Makes a random choice of the questions from the dictionaries
    according to the level given as a parameter
    '''
    if (level == 'easy'):
        question = random.choice(easy_questions)
    else:
        raise ValueError('Invalid level Value')
    answers = question['incorrectAnswers'][:]
    answers.append(question['correctAnswer'])
    random.shuffle(answers)
    selected_question = question['question']
    return selected_question, answers


print(choose_question('easy'))
