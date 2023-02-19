# Movie Trivia Game

# data from the site https://the-trivia-api.com/
easy_questions = [
  {
    "category": "Film & TV",
    "id": "622a1c347cc59eab6f94f901",
    "correctAnswer": "Macauley Culkin",
    "incorrectAnswers": [
      "Bill Murray",
      "Andy Serkis",
      "Al Pacino"
    ],
    "question": "Which actor played the role of Kevin McCallister in Home Alone?",
    "tags": [
      "people",
      "acting",
      "cult_films",
      "film",
      "christmas",
      "general_knowledge",
      "film_and_tv"
    ],
    "type": "Multiple Choice",
    "difficulty": "easy",
    "regions": [],
    "isNiche": False
  },
  {
    "category": "Film & TV",
    "id": "622a1c367cc59eab6f9501f0",
    "correctAnswer": "Christopher Nolan",
    "incorrectAnswers": [
      "Steven Spielberg",
      "Woody Allen",
      "Martin Scorsese"
    ],
    "question": "Which director directed Interstellar?",
    "tags": [
      "film_and_tv"
    ],
    "type": "Multiple Choice",
    "difficulty": "easy",
    "regions": [],
    "isNiche": False
  },
  {
    "category": "Film & TV",
    "id": "622a1c377cc59eab6f950710",
    "correctAnswer": "Will Smith",
    "incorrectAnswers": [
      "Brian Cox",
      "Ralph Fiennes",
      "Ryan Reynolds"
    ],
    "question": "Which actor has starred in films including Men in Black and Enemy of the State?",
    "tags": [
      "film_and_tv"
    ],
    "type": "Multiple Choice",
    "difficulty": "easy",
    "regions": [],
    "isNiche": False
  },
  {
    "category": "Film & TV",
    "id": "625741379da29df7b05f740e",
    "correctAnswer": "Pirates of the Caribbean: The Curse of the Black Pearl",
    "incorrectAnswers": [
      "Die Hard",
      "The Departed",
      "The Truman Show"
    ],
    "question": "Name the movie that matches the following plot summary: 'A blacksmith teams up with an eccentric pirate to save his love.'",
    "tags": [
      "film",
      "film_and_tv"
    ],
    "type": "Multiple Choice",
    "difficulty": "easy",
    "regions": [],
    "isNiche": False
  },
  {
    "category": "Film & TV",
    "id": "62573efd9da29df7b05f7380",
    "correctAnswer": "A man becomes concerned for his Jewish workforce after witnessing their persecution by the Nazis.",
    "incorrectAnswers": [
      "In order to power the city, beasts have to scare children so that they scream.",
      "A girl wanders into a world ruled by gods, witches, and spirits, where humans are changed into beasts.",
      "King Arthur and his Knights embark on a search for a religious relic."
    ],
    "question": "What is the plot of the movie Schindler's List?",
    "tags": [
      "film",
      "film_and_tv"
    ],
    "type": "Multiple Choice",
    "difficulty": "easy",
    "regions": [],
    "isNiche": False
  },
  {
    "category": "Film & TV",
    "id": "622a1c377cc59eab6f950797",
    "correctAnswer": "Robert Downey Jr.",
    "incorrectAnswers": [
      "Chris Evans",
      "Chris Hemsworth",
      "Tom Holland"
    ],
    "question": "Which actor played the role of Iron Man in the Marvel Cinematic Universe?",
    "tags": [
      "acting",
      "film",
      "marvel",
      "comics",
      "mcu",
      "film_and_tv"
    ],
    "type": "Multiple Choice",
    "difficulty": "easy",
    "regions": [],
    "isNiche": False
  },
  {
    "category": "Film & TV",
    "id": "639ae873929b90846f2fc8df",
    "correctAnswer": "Red",
    "incorrectAnswers": [
      "Blue",
      "Green",
      "Purple"
    ],
    "question": "In Star Wars, what color is Darth Vader's lightsaber?",
    "tags": [
      "star_wars",
      "film_and_tv",
      "cult_films",
      "film",
      "science_fiction"
    ],
    "type": "Multiple Choice",
    "difficulty": "easy",
    "regions": [],
    "isNiche": False
  },
  {
    "category": "Film & TV",
    "id": "622a1c347cc59eab6f94fc0f",
    "correctAnswer": "\"Take your stinking paws off me, you damned dirty ape.\"",
    "incorrectAnswers": [
      "\"Mrs. Robinson, you're trying to seduce me. Aren't you?\"",
      "\"Toga! Toga!\"",
      "\"Attica! Attica!\""
    ],
    "question": "Which of these quotes is from the film 'Planet of the Apes'?",
    "tags": [
      "quotes",
      "film",
      "general_knowledge",
      "film_and_tv"
    ],
    "type": "Multiple Choice",
    "difficulty": "easy",
    "regions": [],
    "isNiche": False
  },
  {
    "category": "Film & TV",
    "id": "622a1c347cc59eab6f94fadc",
    "correctAnswer": "Anthony Hopkins",
    "incorrectAnswers": [
      "Warren Beatty",
      "Robert De Niro",
      "Nick Nolte"
    ],
    "question": "Who won the 1991 Academy Award for Best Leading Actor for playing the role of Dr. Hannibal Lecter in The Silence of the Lambs?",
    "tags": [
      "academy_awards",
      "acting",
      "film",
      "general_knowledge",
      "film_and_tv"
    ],
    "type": "Multiple Choice",
    "difficulty": "easy",
    "regions": [],
    "isNiche": False
  },
  {
    "category": "Film & TV",
    "id": "622a1c377cc59eab6f950784",
    "correctAnswer": "Ben Affleck",
    "incorrectAnswers": [
      "Keanu Reeves",
      "Donald Sutherland",
      "Christian Bale"
    ],
    "question": "Which actor has featured in films including Batman v Superman: Dawn of Justice and Argo?",
    "tags": [
      "film_and_tv",
      "film",
      "acting"
    ],
    "type": "Multiple Choice",
    "difficulty": "easy",
    "regions": [],
    "isNiche": False
  },
  {
    "category": "Film & TV",
    "id": "62573fb53d2f5c16bfb88339",
    "correctAnswer": "A cyborg must protect a ten-year-old boy from a more powerful cyborg.",
    "incorrectAnswers": [
      "A criminal pleads insanity and is admitted to a mental institution.",
      "An NYPD officer tries to save his wife taken hostage by terrorists during a Christmas party.",
      "A car salesman's inept crime falls apart due to his and his henchmen's bungling."
    ],
    "question": "What is the plot of the movie Terminator 2: Judgment Day?",
    "tags": [
      "film",
      "film_and_tv"
    ],
    "type": "Multiple Choice",
    "difficulty": "easy",
    "regions": [],
    "isNiche": False
  },
  {
    "category": "Film & TV",
    "id": "622a1c347cc59eab6f94f922",
    "correctAnswer": "Austin Powers: International Man of Mystery",
    "incorrectAnswers": [
      "Die Hard",
      "The Adventures of Robin Hood",
      "Pulp Fiction"
    ],
    "question": "Which film contains the character 'Dr. Evil'?",
    "tags": [
      "acting",
      "film",
      "film_and_tv"
    ],
    "type": "Multiple Choice",
    "difficulty": "easy",
    "regions": [],
    "isNiche": False
  },
  {
    "category": "Film & TV",
    "id": "625740f69da29df7b05f7405",
    "correctAnswer": "Rocky",
    "incorrectAnswers": [
      "Amélie",
      "The Deer Hunter",
      "Schindler's List"
    ],
    "question": "Name the movie that matches the following plot summary: 'A small-time boxer gets a chance to fight the world heavyweight champion.'",
    "tags": [
      "film",
      "film_and_tv"
    ],
    "type": "Multiple Choice",
    "difficulty": "easy",
    "regions": [],
    "isNiche": False
  },
  {
    "category": "Film & TV",
    "id": "622a1c347cc59eab6f94fbe0",
    "correctAnswer": "\"Nobody makes me bleed my own blood. Nobody!\"",
    "incorrectAnswers": [
      "\"Are you not entertained?\"",
      "\"I have had it with these mother—— snakes on this mother—— plane!\"",
      "\"What is this? A center for ants? How can we be expected to teach children to learn how to read…if they can’t even fit inside the building?\""
    ],
    "question": "Which of these quotes is from the film 'Dodgeball: A True Underdog Story'?",
    "tags": [
      "quotes",
      "film",
      "film_and_tv"
    ],
    "type": "Multiple Choice",
    "difficulty": "easy",
    "regions": [],
    "isNiche": False
  },
  {
    "category": "Film & TV",
    "id": "63a03974c7d86251f9b65c5e",
    "correctAnswer": "Ariel",
    "incorrectAnswers": [
      "Belle",
      "Jasmine",
      "Elsa"
    ],
    "question": "What is the name of the mermaid in the Disney film The Little Mermaid?",
    "tags": [
      "film_and_tv",
      "disney",
      "film",
      "fictitious_characters"
    ],
    "type": "Multiple Choice",
    "difficulty": "easy",
    "regions": [],
    "isNiche": False
  },
  {
    "category": "Film & TV",
    "id": "622a1c347cc59eab6f94fc11",
    "correctAnswer": "\"Mrs. Robinson, you're trying to seduce me. Aren't you?\"",
    "incorrectAnswers": [
      "\"Soylent Green is people!\"",
      "\"Round up the usual suspects.\"",
      "\"Just keep swimming.\""
    ],
    "question": "Which of these quotes is from the film 'The Graduate'?",
    "tags": [
      "quotes",
      "film",
      "film_and_tv"
    ],
    "type": "Multiple Choice",
    "difficulty": "easy",
    "regions": [],
    "isNiche": False
  },
  {
    "category": "Film & TV",
    "id": "622a1c347cc59eab6f94fadd",
    "correctAnswer": "Tom Hanks",
    "incorrectAnswers": [
      "Morgan Freeman",
      "Nigel Hawthorne",
      "Paul Newman"
    ],
    "question": "Who won the 1994 Academy Award for Best Leading Actor for playing the role of Forrest Gump in Forrest Gump?",
    "tags": [
      "academy_awards",
      "acting",
      "film",
      "general_knowledge",
      "film_and_tv"
    ],
    "type": "Multiple Choice",
    "difficulty": "easy",
    "regions": [],
    "isNiche": False
  },
  {
    "category": "Film & TV",
    "id": "625741333d2f5c16bfb88345",
    "correctAnswer": "A human soldier is sent from 2029 to 1984 to stop an almost indestructible cyborg killing machine.",
    "incorrectAnswers": [
      "A Marine observes the effects of war on his fellow recruits from their boot camp training to fighting in a war.",
      "The lives of mob hitmen, a boxer, a gangster and his wife, and a pair of bandits intertwine in four tales.",
      "Historical events unfold from the perspective of an Alabama man with an IQ of 75."
    ],
    "question": "What is the plot of the movie The Terminator?",
    "tags": [
      "film",
      "film_and_tv"
    ],
    "type": "Multiple Choice",
    "difficulty": "easy",
    "regions": [],
    "isNiche": False
  },
  {
    "category": "Film & TV",
    "id": "622a1c347cc59eab6f94fa61",
    "correctAnswer": "Heath Ledger",
    "incorrectAnswers": [
      "Josh Brolin",
      "Robert Downey Jr.",
      "Philip Seymour Hoffman"
    ],
    "question": "Who won the 2008 Academy Award for Best Supporting Actor for playing the role of Joker in The Dark Knight?",
    "tags": [
      "academy_awards",
      "film",
      "batman",
      "dc",
      "comics",
      "acting",
      "general_knowledge",
      "film_and_tv"
    ],
    "type": "Multiple Choice",
    "difficulty": "easy",
    "regions": [],
    "isNiche": False
  },
  {
    "category": "Film & TV",
    "id": "625740939da29df7b05f73e8",
    "correctAnswer": "A paleontologist is tasked with protecting two children when cloned dinosaurs are set free.",
    "incorrectAnswers": [
      "During WWII a Jewish waiter uses humor to protect his son from the realities of war.",
      "A maverick teacher emboldens his students to new heights of self-expression.",
      "A car salesman's inept crime falls apart due to his and his henchmen's bungling."
    ],
    "question": "What is the plot of the movie Jurassic Park?",
    "tags": [
      "film",
      "film_and_tv"
    ],
    "type": "Multiple Choice",
    "difficulty": "easy",
    "regions": [],
    "isNiche": False
  }
]

print(easy_questions[0]['question'])
print(easy_questions[0]['correctAnswer'])
print(easy_questions[0]['incorrectAnswers'])