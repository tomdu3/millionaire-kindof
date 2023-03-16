# import questions from different API https://opentdb.com/api_config.php
import requests

params = {
    'amount': 15,
    'category': 11,
    'type': 'multiple',
}

difficulty_choice = ['easy', 'medium', 'hard']
questions = []
for difficulty in difficulty_choice:
    parameters = {item:value for item,value in params.items()}
    parameters['difficulty'] = difficulty

    r = requests.get('https://opentdb.com/api.php', params=parameters)
    r.raise_for_status()
    data = r.json()
    questions.append(data["results"])

easy_questions = questions[0]
medium_questions = questions[1]
hard_questions = questions[2]

print(easy_questions)
print(medium_questions)
print(hard_questions)