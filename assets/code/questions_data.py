import json

# data from the site https://the-trivia-api.com/
with open('./assets/json/easy.json', 'r') as f:
    easy_questions = json.load(f)['0']
with open('./assets/json/medium.json', 'r') as f:
    medium_questions = json.load(f)['0']
with open('./assets/json/hard.json', 'r') as f:
    hard_questions = json.load(f)['0']

question_points = {
  1: 100,
  2: 200,
  3: 300,
  4: 500,
  5: 1000,
  6: 2000,
  7: 4000,
  8: 8000,
  9: 16000,
  10: 32000,
  11: 64000,
  12: 125000,
  13: 240000,
  14: 500000,
  15: 1000000,
}
