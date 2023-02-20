# Movie Trivia Game


from questions import *
import random


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


def display_question(question_num, question, answers, correct_answer_index):
    '''
    The function displays the question by writing a question order number,
    the question itself and all the answers. It asks for a user to
    select the correct answer and gives the output for the wrong/write
    answer.
    '''
    print(f'Question No. {question_num}:\n\n')
    print(question, '\n\n')
    print('Choose a correct answer: \n')
    abc = ['a', 'b', 'c', 'd']
    for i in range(4):
        print(f'{abc[i]}. {answers[i]}\n')
    while True:
        answer = input('Choose a, b, c, or d: \n')
        if answer.lower() not in abc:
            print("\n Invalid input! Please, do as you're told! \n")
            continue
        else:
            break
    if abc.index(answer) != correct_answer_index:
        print(f'That is not the right answer. Right answer is {abc[correct_answer_index]}')
    else:
        print(f"You're good! Well done.")


(select_question, all_answers, corr_index) = choose_question('hard')
display_question(1, select_question, all_answers, corr_index)

