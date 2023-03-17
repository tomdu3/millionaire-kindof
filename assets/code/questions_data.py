import json

# data from the site https://the-trivia-api.com/
with open('./assets/code/easy.json', 'r') as f:
    easy_questions = json.load(f)['0']
with open('./assets/code/medium.json', 'r') as f:
    medium_questions = json.load(f)['0']
with open('./assets/code/hard.json', 'r') as f:
    hard_questions = json.load(f)['0']




# easy_questions = [
#   {
#     "category": "Film & TV",
#     "id": "622a1c347cc59eab6f94f901",
#     "correctAnswer": "Macauley Culkin",
#     "incorrectAnswers": [
#       "Bill Murray",
#       "Andy Serkis",
#       "Al Pacino"
#     ],
#     "question": "Which actor played the role of Kevin McCallister in Home Alone?",
#     "tags": [
#       "people",
#       "acting",
#       "cult_films",
#       "film",
#       "christmas",
#       "general_knowledge",
#       "film_and_tv"
#     ],
#     "type": "Multiple Choice",
#     "difficulty": "easy",
#     "regions": [],
#     "isNiche": False
#   },
#   {
#     "category": "Film & TV",
#     "id": "622a1c367cc59eab6f9501f0",
#     "correctAnswer": "Christopher Nolan",
#     "incorrectAnswers": [
#       "Steven Spielberg",
#       "Woody Allen",
#       "Martin Scorsese"
#     ],
#     "question": "Which director directed Interstellar?",
#     "tags": [
#       "film_and_tv"
#     ],
#     "type": "Multiple Choice",
#     "difficulty": "easy",
#     "regions": [],
#     "isNiche": False
#   },
#   {
#     "category": "Film & TV",
#     "id": "622a1c377cc59eab6f950710",
#     "correctAnswer": "Will Smith",
#     "incorrectAnswers": [
#       "Brian Cox",
#       "Ralph Fiennes",
#       "Ryan Reynolds"
#     ],
#     "question": "Which actor has starred in films including Men in Black and Enemy of the State?",
#     "tags": [
#       "film_and_tv"
#     ],
#     "type": "Multiple Choice",
#     "difficulty": "easy",
#     "regions": [],
#     "isNiche": False
#   },
#   {
#     "category": "Film & TV",
#     "id": "625741379da29df7b05f740e",
#     "correctAnswer": "Pirates of the Caribbean: The Curse of the Black Pearl",
#     "incorrectAnswers": [
#       "Die Hard",
#       "The Departed",
#       "The Truman Show"
#     ],
#     "question": "Name the movie that matches the following plot summary: 'A blacksmith teams up with an eccentric pirate to save his love.'",
#     "tags": [
#       "film",
#       "film_and_tv"
#     ],
#     "type": "Multiple Choice",
#     "difficulty": "easy",
#     "regions": [],
#     "isNiche": False
#   },
#   {
#     "category": "Film & TV",
#     "id": "62573efd9da29df7b05f7380",
#     "correctAnswer": "A man becomes concerned for his Jewish workforce after witnessing their persecution by the Nazis.",
#     "incorrectAnswers": [
#       "In order to power the city, beasts have to scare children so that they scream.",
#       "A girl wanders into a world ruled by gods, witches, and spirits, where humans are changed into beasts.",
#       "King Arthur and his Knights embark on a search for a religious relic."
#     ],
#     "question": "What is the plot of the movie Schindler's List?",
#     "tags": [
#       "film",
#       "film_and_tv"
#     ],
#     "type": "Multiple Choice",
#     "difficulty": "easy",
#     "regions": [],
#     "isNiche": False
#   },
#   {
#     "category": "Film & TV",
#     "id": "622a1c377cc59eab6f950797",
#     "correctAnswer": "Robert Downey Jr.",
#     "incorrectAnswers": [
#       "Chris Evans",
#       "Chris Hemsworth",
#       "Tom Holland"
#     ],
#     "question": "Which actor played the role of Iron Man in the Marvel Cinematic Universe?",
#     "tags": [
#       "acting",
#       "film",
#       "marvel",
#       "comics",
#       "mcu",
#       "film_and_tv"
#     ],
#     "type": "Multiple Choice",
#     "difficulty": "easy",
#     "regions": [],
#     "isNiche": False
#   },
#   {
#     "category": "Film & TV",
#     "id": "639ae873929b90846f2fc8df",
#     "correctAnswer": "Red",
#     "incorrectAnswers": [
#       "Blue",
#       "Green",
#       "Purple"
#     ],
#     "question": "In Star Wars, what color is Darth Vader's lightsaber?",
#     "tags": [
#       "star_wars",
#       "film_and_tv",
#       "cult_films",
#       "film",
#       "science_fiction"
#     ],
#     "type": "Multiple Choice",
#     "difficulty": "easy",
#     "regions": [],
#     "isNiche": False
#   },
#   {
#     "category": "Film & TV",
#     "id": "622a1c347cc59eab6f94fc0f",
#     "correctAnswer": "\"Take your stinking paws off me, you damned dirty ape.\"",
#     "incorrectAnswers": [
#       "\"Mrs. Robinson, you're trying to seduce me. Aren't you?\"",
#       "\"Toga! Toga!\"",
#       "\"Attica! Attica!\""
#     ],
#     "question": "Which of these quotes is from the film 'Planet of the Apes'?",
#     "tags": [
#       "quotes",
#       "film",
#       "general_knowledge",
#       "film_and_tv"
#     ],
#     "type": "Multiple Choice",
#     "difficulty": "easy",
#     "regions": [],
#     "isNiche": False
#   },
#   {
#     "category": "Film & TV",
#     "id": "622a1c347cc59eab6f94fadc",
#     "correctAnswer": "Anthony Hopkins",
#     "incorrectAnswers": [
#       "Warren Beatty",
#       "Robert De Niro",
#       "Nick Nolte"
#     ],
#     "question": "Who won the 1991 Academy Award for Best Leading Actor for playing the role of Dr. Hannibal Lecter in The Silence of the Lambs?",
#     "tags": [
#       "academy_awards",
#       "acting",
#       "film",
#       "general_knowledge",
#       "film_and_tv"
#     ],
#     "type": "Multiple Choice",
#     "difficulty": "easy",
#     "regions": [],
#     "isNiche": False
#   },
#   {
#     "category": "Film & TV",
#     "id": "622a1c377cc59eab6f950784",
#     "correctAnswer": "Ben Affleck",
#     "incorrectAnswers": [
#       "Keanu Reeves",
#       "Donald Sutherland",
#       "Christian Bale"
#     ],
#     "question": "Which actor has featured in films including Batman v Superman: Dawn of Justice and Argo?",
#     "tags": [
#       "film_and_tv",
#       "film",
#       "acting"
#     ],
#     "type": "Multiple Choice",
#     "difficulty": "easy",
#     "regions": [],
#     "isNiche": False
#   },
#   {
#     "category": "Film & TV",
#     "id": "62573fb53d2f5c16bfb88339",
#     "correctAnswer": "A cyborg must protect a ten-year-old boy from a more powerful cyborg.",
#     "incorrectAnswers": [
#       "A criminal pleads insanity and is admitted to a mental institution.",
#       "An NYPD officer tries to save his wife taken hostage by terrorists during a Christmas party.",
#       "A car salesman's inept crime falls apart due to his and his henchmen's bungling."
#     ],
#     "question": "What is the plot of the movie Terminator 2: Judgment Day?",
#     "tags": [
#       "film",
#       "film_and_tv"
#     ],
#     "type": "Multiple Choice",
#     "difficulty": "easy",
#     "regions": [],
#     "isNiche": False
#   },
#   {
#     "category": "Film & TV",
#     "id": "622a1c347cc59eab6f94f922",
#     "correctAnswer": "Austin Powers: International Man of Mystery",
#     "incorrectAnswers": [
#       "Die Hard",
#       "The Adventures of Robin Hood",
#       "Pulp Fiction"
#     ],
#     "question": "Which film contains the character 'Dr. Evil'?",
#     "tags": [
#       "acting",
#       "film",
#       "film_and_tv"
#     ],
#     "type": "Multiple Choice",
#     "difficulty": "easy",
#     "regions": [],
#     "isNiche": False
#   },
#   {
#     "category": "Film & TV",
#     "id": "625740f69da29df7b05f7405",
#     "correctAnswer": "Rocky",
#     "incorrectAnswers": [
#       "Amélie",
#       "The Deer Hunter",
#       "Schindler's List"
#     ],
#     "question": "Name the movie that matches the following plot summary: 'A small-time boxer gets a chance to fight the world heavyweight champion.'",
#     "tags": [
#       "film",
#       "film_and_tv"
#     ],
#     "type": "Multiple Choice",
#     "difficulty": "easy",
#     "regions": [],
#     "isNiche": False
#   },
#   {
#     "category": "Film & TV",
#     "id": "622a1c347cc59eab6f94fbe0",
#     "correctAnswer": "\"Nobody makes me bleed my own blood. Nobody!\"",
#     "incorrectAnswers": [
#       "\"Are you not entertained?\"",
#       "\"I have had it with these mother—— snakes on this mother—— plane!\"",
#       "\"What is this? A center for ants? How can we be expected to teach children to learn how to read…if they can’t even fit inside the building?\""
#     ],
#     "question": "Which of these quotes is from the film 'Dodgeball: A True Underdog Story'?",
#     "tags": [
#       "quotes",
#       "film",
#       "film_and_tv"
#     ],
#     "type": "Multiple Choice",
#     "difficulty": "easy",
#     "regions": [],
#     "isNiche": False
#   },
#   {
#     "category": "Film & TV",
#     "id": "63a03974c7d86251f9b65c5e",
#     "correctAnswer": "Ariel",
#     "incorrectAnswers": [
#       "Belle",
#       "Jasmine",
#       "Elsa"
#     ],
#     "question": "What is the name of the mermaid in the Disney film The Little Mermaid?",
#     "tags": [
#       "film_and_tv",
#       "disney",
#       "film",
#       "fictitious_characters"
#     ],
#     "type": "Multiple Choice",
#     "difficulty": "easy",
#     "regions": [],
#     "isNiche": False
#   },
#   {
#     "category": "Film & TV",
#     "id": "622a1c347cc59eab6f94fc11",
#     "correctAnswer": "\"Mrs. Robinson, you're trying to seduce me. Aren't you?\"",
#     "incorrectAnswers": [
#       "\"Soylent Green is people!\"",
#       "\"Round up the usual suspects.\"",
#       "\"Just keep swimming.\""
#     ],
#     "question": "Which of these quotes is from the film 'The Graduate'?",
#     "tags": [
#       "quotes",
#       "film",
#       "film_and_tv"
#     ],
#     "type": "Multiple Choice",
#     "difficulty": "easy",
#     "regions": [],
#     "isNiche": False
#   },
#   {
#     "category": "Film & TV",
#     "id": "622a1c347cc59eab6f94fadd",
#     "correctAnswer": "Tom Hanks",
#     "incorrectAnswers": [
#       "Morgan Freeman",
#       "Nigel Hawthorne",
#       "Paul Newman"
#     ],
#     "question": "Who won the 1994 Academy Award for Best Leading Actor for playing the role of Forrest Gump in Forrest Gump?",
#     "tags": [
#       "academy_awards",
#       "acting",
#       "film",
#       "general_knowledge",
#       "film_and_tv"
#     ],
#     "type": "Multiple Choice",
#     "difficulty": "easy",
#     "regions": [],
#     "isNiche": False
#   },
#   {
#     "category": "Film & TV",
#     "id": "625741333d2f5c16bfb88345",
#     "correctAnswer": "A human soldier is sent from 2029 to 1984 to stop an almost indestructible cyborg killing machine.",
#     "incorrectAnswers": [
#       "A Marine observes the effects of war on his fellow recruits from their boot camp training to fighting in a war.",
#       "The lives of mob hitmen, a boxer, a gangster and his wife, and a pair of bandits intertwine in four tales.",
#       "Historical events unfold from the perspective of an Alabama man with an IQ of 75."
#     ],
#     "question": "What is the plot of the movie The Terminator?",
#     "tags": [
#       "film",
#       "film_and_tv"
#     ],
#     "type": "Multiple Choice",
#     "difficulty": "easy",
#     "regions": [],
#     "isNiche": False
#   },
#   {
#     "category": "Film & TV",
#     "id": "622a1c347cc59eab6f94fa61",
#     "correctAnswer": "Heath Ledger",
#     "incorrectAnswers": [
#       "Josh Brolin",
#       "Robert Downey Jr.",
#       "Philip Seymour Hoffman"
#     ],
#     "question": "Who won the 2008 Academy Award for Best Supporting Actor for playing the role of Joker in The Dark Knight?",
#     "tags": [
#       "academy_awards",
#       "film",
#       "batman",
#       "dc",
#       "comics",
#       "acting",
#       "general_knowledge",
#       "film_and_tv"
#     ],
#     "type": "Multiple Choice",
#     "difficulty": "easy",
#     "regions": [],
#     "isNiche": False
#   },
#   {
#     "category": "Film & TV",
#     "id": "625740939da29df7b05f73e8",
#     "correctAnswer": "A paleontologist is tasked with protecting two children when cloned dinosaurs are set free.",
#     "incorrectAnswers": [
#       "During WWII a Jewish waiter uses humor to protect his son from the realities of war.",
#       "A maverick teacher emboldens his students to new heights of self-expression.",
#       "A car salesman's inept crime falls apart due to his and his henchmen's bungling."
#     ],
#     "question": "What is the plot of the movie Jurassic Park?",
#     "tags": [
#       "film",
#       "film_and_tv"
#     ],
#     "type": "Multiple Choice",
#     "difficulty": "easy",
#     "regions": [],
#     "isNiche": False
#   }
# ]

# medium_questions = [
#   {
#     "category": "Film & TV",
#     "id": "6257407f9da29df7b05f73e2",
#     "correctAnswer": "After a girl is uprooted from her life, her emotions conflict on how best to navigate a new life.",
#     "incorrectAnswers": [
#       "A slacker seeks restitution for a rug ruined by debt collectors.",
#       "POWs are forced to build a railway, not knowing that allies are planning to destroy it.",
#       "In a post-apocalyptic wasteland, a woman rebels against a tyrannical ruler."
#     ],
#     "question": "What is the plot of the movie Inside Out?",
#     "tags": [
#       "film",
#       "film_and_tv"
#     ],
#     "type": "Multiple Choice",
#     "difficulty": "medium",
#     "regions": [],
#     "isNiche": False
#   },
#   {
#     "category": "Film & TV",
#     "id": "622a1c347cc59eab6f94fafc",
#     "correctAnswer": "Natalie Portman",
#     "incorrectAnswers": [
#       "Annette Bening",
#       "Nicole Kidman",
#       "Jennifer Lawrence"
#     ],
#     "question": "Who won the 2010 Academy Award for Best Leading Actress for playing the role of Nina Sayers/The Swan Queen in Black Swan?",
#     "tags": [
#       "acting",
#       "film",
#       "academy_awards",
#       "film_and_tv"
#     ],
#     "type": "Multiple Choice",
#     "difficulty": "medium",
#     "regions": [],
#     "isNiche": False
#   },
#   {
#     "category": "Film & TV",
#     "id": "622a1c377cc59eab6f95078b",
#     "correctAnswer": "Gary Oldman",
#     "incorrectAnswers": [
#       "James Franco",
#       "George Clooney",
#       "Laurence Fishburne"
#     ],
#     "question": "Which actor has starred in both Harry Potter and Batman Begins?",
#     "tags": [
#       "film",
#       "acting",
#       "film_and_tv"
#     ],
#     "type": "Multiple Choice",
#     "difficulty": "medium",
#     "regions": [],
#     "isNiche": False
#   },
#   {
#     "category": "Film & TV",
#     "id": "62573f419da29df7b05f7390",
#     "correctAnswer": "It's a Wonderful Life",
#     "incorrectAnswers": [
#       "WALL·E",
#       "Ratatouille",
#       "Psycho"
#     ],
#     "question": "Name the movie that matches the following plot summary: 'An angel is sent to help a man by showing him what life would have been like if he had never existed.'",
#     "tags": [
#       "film",
#       "film_and_tv"
#     ],
#     "type": "Multiple Choice",
#     "difficulty": "medium",
#     "regions": [],
#     "isNiche": False
#   },
#   {
#     "category": "Film & TV",
#     "id": "63a0396fc7d86251f9b65c58",
#     "correctAnswer": "Scamp",
#     "incorrectAnswers": [
#       "Sparky",
#       "Max",
#       "Bolt"
#     ],
#     "question": "What is the name of the dog in the movie Lady and the Tramp?",
#     "tags": [
#       "film_and_tv",
#       "disney",
#       "film",
#       "animals",
#       "dogs"
#     ],
#     "type": "Multiple Choice",
#     "difficulty": "medium",
#     "regions": [],
#     "isNiche": False
#   },
#   {
#     "category": "Film & TV",
#     "id": "625fd74bdc0dd3b72da64d31",
#     "correctAnswer": "2003",
#     "incorrectAnswers": [
#       "2000",
#       "2006",
#       "2009"
#     ],
#     "question": "In which year was Pirates of the Caribbean: The Curse of the Black Pearl first released in the cinema?",
#     "tags": [
#       "film",
#       "film_and_tv"
#     ],
#     "type": "Multiple Choice",
#     "difficulty": "medium",
#     "regions": [],
#     "isNiche": False
#   },
#   {
#     "category": "Film & TV",
#     "id": "622a1c377cc59eab6f95070e",
#     "correctAnswer": "Charlize Theron",
#     "incorrectAnswers": [
#       "Sandra Bæ Hovedr",
#       "Kirsten Dunst",
#       "Emma Thompson"
#     ],
#     "question": "Which actor has featued in films including Mad Max: Fury Road and Prometheus?",
#     "tags": [
#       "acting",
#       "film",
#       "film_and_tv"
#     ],
#     "type": "Multiple Choice",
#     "difficulty": "medium",
#     "regions": [],
#     "isNiche": False
#   },
#   {
#     "category": "Film & TV",
#     "id": "622a1c367cc59eab6f950404",
#     "correctAnswer": "Halloween",
#     "incorrectAnswers": [
#       "A Nightmare on Elm Street",
#       "Scream",
#       "Child's Play"
#     ],
#     "question": "The Character Of Mike Myers Features Heavily In Which Series Of Horror Movies?",
#     "tags": [
#       "film_and_tv"
#     ],
#     "type": "Multiple Choice",
#     "difficulty": "medium",
#     "regions": [],
#     "isNiche": False
#   },
#   {
#     "category": "Film & TV",
#     "id": "62573f789da29df7b05f739e",
#     "correctAnswer": "The Departed",
#     "incorrectAnswers": [
#       "Double Indemnity",
#       "Indiana Jones and the Last Crusade",
#       "Groundhog Day"
#     ],
#     "question": "Name the movie that matches the following plot summary: 'An undercover cop and a mole in the police try to identify each other while infiltrating a gang.'",
#     "tags": [
#       "film",
#       "film_and_tv"
#     ],
#     "type": "Multiple Choice",
#     "difficulty": "medium",
#     "regions": [],
#     "isNiche": False
#   },
#   {
#     "category": "Film & TV",
#     "id": "622a1c377cc59eab6f950729",
#     "correctAnswer": "Kate Winslet",
#     "incorrectAnswers": [
#       "Kathy Bates",
#       "Kirsten Dunst",
#       "Sandra Bæ Hovedr"
#     ],
#     "question": "Which actor has featued in films including Titanic and The Reader?",
#     "tags": [
#       "film_and_tv"
#     ],
#     "type": "Multiple Choice",
#     "difficulty": "medium",
#     "regions": [],
#     "isNiche": False
#   },
#   {
#     "category": "Film & TV",
#     "id": "622a1c347cc59eab6f94fbe8",
#     "correctAnswer": "\"Exercise gives you endorphins. Endorphins make you happy. Happy people just don’t shoot their husbands. They just don’t.\"",
#     "incorrectAnswers": [
#       "\"I'm gonna make him an offer he can't refuse.\"",
#       "\"I’m not drinking any f****** Merlot!\"",
#       "\"Listen to them. Children of the night. What music they make.\""
#     ],
#     "question": "Which of these quotes is from the film 'Legally Blonde'?",
#     "tags": [
#       "quotes",
#       "film",
#       "film_and_tv"
#     ],
#     "type": "Multiple Choice",
#     "difficulty": "medium",
#     "regions": [],
#     "isNiche": False
#   },
#   {
#     "category": "Film & TV",
#     "id": "625fd66bdc0dd3b72da64cef",
#     "correctAnswer": "1980",
#     "incorrectAnswers": [
#       "1965",
#       "1970",
#       "1975"
#     ],
#     "question": "In which year was Star Wars: Episode V - The Empire Strikes Back first released in the cinema?",
#     "tags": [
#       "film",
#       "cult_films",
#       "star_wars",
#       "film_and_tv"
#     ],
#     "type": "Multiple Choice",
#     "difficulty": "medium",
#     "regions": [],
#     "isNiche": False
#   },
#   {
#     "category": "Film & TV",
#     "id": "622a1c367cc59eab6f950401",
#     "correctAnswer": "Taxi Driver",
#     "incorrectAnswers": [
#       "The Graduate",
#       "Midnight Cowboy",
#       "Raging Bull"
#     ],
#     "question": "'You talkin to me?' is a line from which 1970's film?",
#     "tags": [
#       "film",
#       "quotes",
#       "film_and_tv"
#     ],
#     "type": "Multiple Choice",
#     "difficulty": "medium",
#     "regions": [],
#     "isNiche": False
#   },
#   {
#     "category": "Film & TV",
#     "id": "62573f0b9da29df7b05f7384",
#     "correctAnswer": "Inception",
#     "incorrectAnswers": [
#       "A Beautiful Mind",
#       "The Sixth Sense",
#       "A Clockwork Orange"
#     ],
#     "question": "Name the movie that matches the following plot summary: 'A thief who steals secrets through dreams must plant an idea into the mind of a C.E.O.'",
#     "tags": [
#       "film",
#       "film_and_tv"
#     ],
#     "type": "Multiple Choice",
#     "difficulty": "medium",
#     "regions": [],
#     "isNiche": False
#   },
#   {
#     "category": "Film & TV",
#     "id": "622a1c377cc59eab6f9506f9",
#     "correctAnswer": "Matthew McConaughey",
#     "incorrectAnswers": [
#       "Ryan Reynolds",
#       "Jim Carrey",
#       "Hugh Jackman"
#     ],
#     "question": "Which actor has featued in films including The Wolf of Wall Street and Dallas Buyers Club?",
#     "tags": [
#       "film_and_tv"
#     ],
#     "type": "Multiple Choice",
#     "difficulty": "medium",
#     "regions": [],
#     "isNiche": False
#   },
#   {
#     "category": "Film & TV",
#     "id": "624db9e8de6018633d31f6aa",
#     "correctAnswer": "Daniel Craig",
#     "incorrectAnswers": [
#       "Roger Moore",
#       "Sean Connery",
#       "Timothy Dalton"
#     ],
#     "question": "Who played the role of James Bond in Spectre?",
#     "tags": [
#       "james_bond",
#       "film",
#       "acting",
#       "film_and_tv"
#     ],
#     "type": "Multiple Choice",
#     "difficulty": "medium",
#     "regions": [],
#     "isNiche": False
#   },
#   {
#     "category": "Film & TV",
#     "id": "622a1c3c7cc59eab6f951a32",
#     "correctAnswer": "Treehouse of Horror",
#     "incorrectAnswers": [
#       "Spooky Springfield",
#       "The Halloween Haunt",
#       "Evergreen Menace"
#     ],
#     "question": "What are The Simpsons Halloween specials known as?",
#     "tags": [
#       "film_and_tv"
#     ],
#     "type": "Multiple Choice",
#     "difficulty": "medium",
#     "regions": [],
#     "isNiche": False
#   },
#   {
#     "category": "Film & TV",
#     "id": "625740139da29df7b05f73c2",
#     "correctAnswer": "To Kill a Mockingbird",
#     "incorrectAnswers": [
#       "Cool Hand Luke",
#       "The Elephant Man",
#       "The Lion King"
#     ],
#     "question": "Name the movie that matches the following plot summary: 'A lawyer in Depression-era Alabama defends a black man against an undeserved rape charge.'",
#     "tags": [
#       "film",
#       "film_and_tv"
#     ],
#     "type": "Multiple Choice",
#     "difficulty": "medium",
#     "regions": [],
#     "isNiche": False
#   },
#   {
#     "category": "Film & TV",
#     "id": "622a1c377cc59eab6f950678",
#     "correctAnswer": "Hugo Weaving",
#     "incorrectAnswers": [
#       "Tobey Maguire",
#       "Timothy Spall",
#       "Elijah Wood"
#     ],
#     "question": "Which actor starred in films including The Lord of the Rings and The Matrix?",
#     "tags": [
#       "acting",
#       "film",
#       "film_and_tv"
#     ],
#     "type": "Multiple Choice",
#     "difficulty": "medium",
#     "regions": [],
#     "isNiche": False
#   },
#   {
#     "category": "Film & TV",
#     "id": "625699009da29df7b05f72ab",
#     "correctAnswer": "The Collector",
#     "incorrectAnswers": [
#       "Alexander Pierce",
#       "Howard Stark",
#       "Groot"
#     ],
#     "question": "In the Marvel Cinematic Unvierse, which character is played by Benicio Del Toro?",
#     "tags": [
#       "mcu",
#       "film",
#       "acting",
#       "marvel",
#       "comics",
#       "film_and_tv"
#     ],
#     "type": "Multiple Choice",
#     "difficulty": "medium",
#     "regions": [],
#     "isNiche": False
#   }
# ]

# hard_questions = [
#   {
#     "category": "Film & TV",
#     "id": "622a1c377cc59eab6f950658",
#     "correctAnswer": "Anthony Quinn",
#     "incorrectAnswers": [
#       "James Hong",
#       "Gary Cooper",
#       "Sam Shepard"
#     ],
#     "question": "Which actor has featued in films including Lawrence of Arabia and La Strada?",
#     "tags": [
#       "film",
#       "acting",
#       "film_and_tv"
#     ],
#     "type": "Multiple Choice",
#     "difficulty": "hard",
#     "regions": [],
#     "isNiche": False
#   },
#   {
#     "category": "Film & TV",
#     "id": "625fd64ddc0dd3b72da64ce6",
#     "correctAnswer": "1972",
#     "incorrectAnswers": [
#       "1954",
#       "1960",
#       "1966"
#     ],
#     "question": "In which year was The Godfather released?",
#     "tags": [
#       "film",
#       "film_and_tv"
#     ],
#     "type": "Multiple Choice",
#     "difficulty": "hard",
#     "regions": [],
#     "isNiche": False
#   },
#   {
#     "category": "Film & TV",
#     "id": "622a1c377cc59eab6f950668",
#     "correctAnswer": "Dennis Hopper",
#     "incorrectAnswers": [
#       "Tim Roth",
#       "Hugo Weaving",
#       "Warwick Davis"
#     ],
#     "question": "Which actor has featued in films including Apocalypse Now and Speed?",
#     "tags": [
#       "acting",
#       "film",
#       "film_and_tv"
#     ],
#     "type": "Multiple Choice",
#     "difficulty": "hard",
#     "regions": [],
#     "isNiche": False
#   },
#   {
#     "category": "Film & TV",
#     "id": "622a1c347cc59eab6f94fa83",
#     "correctAnswer": "Christopher Walken",
#     "incorrectAnswers": [
#       "Bruce Dern",
#       "Richard Farnsworth",
#       "John Hurt"
#     ],
#     "question": "Who won the 1978 Academy Award for Best Supporting Actor for playing the role of Nick in The Deer Hunter?",
#     "tags": [
#       "acting",
#       "cult_films",
#       "academy_awards",
#       "film_and_tv"
#     ],
#     "type": "Multiple Choice",
#     "difficulty": "hard",
#     "regions": [],
#     "isNiche": False
#   },
#   {
#     "category": "Film & TV",
#     "id": "622a1c377cc59eab6f9506a3",
#     "correctAnswer": "Melissa Leo",
#     "incorrectAnswers": [
#       "Naomi Watts",
#       "Keira Knightley",
#       "Kristin Scott Thomas"
#     ],
#     "question": "Which actor has featued in films including Cold Case and Veronica Mars?",
#     "tags": [
#       "film_and_tv"
#     ],
#     "type": "Multiple Choice",
#     "difficulty": "hard",
#     "regions": [],
#     "isNiche": False
#   },
#   {
#     "category": "Film & TV",
#     "id": "622a1c367cc59eab6f9501e0",
#     "correctAnswer": "Sidney Lumet",
#     "incorrectAnswers": [
#       "Steven Spielberg",
#       "Woody Allen",
#       "Martin Scorsese"
#     ],
#     "question": "Which director directed 12 Angry Men?",
#     "tags": [
#       "film_and_tv"
#     ],
#     "type": "Multiple Choice",
#     "difficulty": "hard",
#     "regions": [],
#     "isNiche": False
#   },
#   {
#     "category": "Film & TV",
#     "id": "622a1c377cc59eab6f950674",
#     "correctAnswer": "Jack Lemmon",
#     "incorrectAnswers": [
#       "Timothy Spall",
#       "Hugo Weaving",
#       "Tim Roth"
#     ],
#     "question": "Which actor has featued in films including Some Like It Hot and JFK?",
#     "tags": [
#       "film_and_tv"
#     ],
#     "type": "Multiple Choice",
#     "difficulty": "hard",
#     "regions": [],
#     "isNiche": False
#   },
#   {
#     "category": "Film & TV",
#     "id": "622a1c347cc59eab6f94fa6e",
#     "correctAnswer": "Morgan Freeman",
#     "incorrectAnswers": [
#       "Alan Alda",
#       "Thomas Haden Church",
#       "Jamie Foxx"
#     ],
#     "question": "Who won the 2004 Academy Award for Best Supporting Actor for playing the role of Eddie Scrap-Iron Dupris in Million Dollar Baby?",
#     "tags": [
#       "academy_awards",
#       "film",
#       "film_and_tv"
#     ],
#     "type": "Multiple Choice",
#     "difficulty": "hard",
#     "regions": [],
#     "isNiche": False
#   },
#   {
#     "category": "Film & TV",
#     "id": "63dd25e3742e43ed64f1f040",
#     "correctAnswer": "Niles Crane",
#     "incorrectAnswers": [
#       "Frasier Moon",
#       "Roz Doyle",
#       "Martin Crane"
#     ],
#     "question": "What is the name of the character played by David Hyde Pierce on the show 'Frasier'?",
#     "tags": [
#       "film_and_tv",
#       "tv",
#       "sitcoms"
#     ],
#     "type": "Multiple Choice",
#     "difficulty": "hard",
#     "regions": [],
#     "isNiche": False
#   },
#   {
#     "category": "Film & TV",
#     "id": "622a1c347cc59eab6f94fa65",
#     "correctAnswer": "Christoph Waltz",
#     "incorrectAnswers": [
#       "Alan Arkin",
#       "Robert De Niro",
#       "Philip Seymour Hoffman"
#     ],
#     "question": "Who won the 2012 Academy Award for Best Supporting Actor for playing the role of Dr. King Schultz in Django Unchained?",
#     "tags": [
#       "academy_awards",
#       "acting",
#       "film",
#       "film_and_tv"
#     ],
#     "type": "Multiple Choice",
#     "difficulty": "hard",
#     "regions": [],
#     "isNiche": False
#   },
#   {
#     "category": "Film & TV",
#     "id": "622a1c357cc59eab6f94fc46",
#     "correctAnswer": "\"You talking to me?\"",
#     "incorrectAnswers": [
#       "\"It's alive! It's alive!\"",
#       "\"Attica! Attica!\"",
#       "\"After all, tomorrow is another day!\""
#     ],
#     "question": "Which of these quotes is from the film 'Taxi Driver'?",
#     "tags": [
#       "quotes",
#       "film",
#       "film_and_tv"
#     ],
#     "type": "Multiple Choice",
#     "difficulty": "hard",
#     "regions": [],
#     "isNiche": False
#   },
#   {
#     "category": "Film & TV",
#     "id": "622a1c347cc59eab6f94fad6",
#     "correctAnswer": "Roberto Benigni",
#     "incorrectAnswers": [
#       "Tom Hanks",
#       "Ian McKellen",
#       "Nick Nolte"
#     ],
#     "question": "Who won the 1998 Academy Award for Best Leading Actor for playing the role of Guido in Life Is Beautiful?",
#     "tags": [
#       "academy_awards",
#       "film",
#       "film_and_tv"
#     ],
#     "type": "Multiple Choice",
#     "difficulty": "hard",
#     "regions": [],
#     "isNiche": False
#   },
#   {
#     "category": "Film & TV",
#     "id": "625740af9da29df7b05f73f0",
#     "correctAnswer": "After he becomes a quadriplegic, an aristocrat hires a young man to be his caregiver.",
#     "incorrectAnswers": [
#       "A naive youth leader is appointed to fill a vacancy in the U.S. Senate.",
#       "An archaeologist is hired by the government to find the Ark of the Covenant.",
#       "When a serial killer murders key political figures, a vigilante is forced to intervene."
#     ],
#     "question": "What is the plot of the movie Untouchable?",
#     "tags": [
#       "film",
#       "film_and_tv"
#     ],
#     "type": "Multiple Choice",
#     "difficulty": "hard",
#     "regions": [],
#     "isNiche": False
#   },
#   {
#     "category": "Film & TV",
#     "id": "622a1c377cc59eab6f95065d",
#     "correctAnswer": "Timothy Spall",
#     "incorrectAnswers": [
#       "Paul Newman",
#       "Tobey Maguire",
#       "Dennis Hopper"
#     ],
#     "question": "Which actor has featued in films including Harry Potter and the Goblet of Fire and Lemony Snicket's A Series of Unfortunate Events?",
#     "tags": [
#       "film_and_tv"
#     ],
#     "type": "Multiple Choice",
#     "difficulty": "hard",
#     "regions": [],
#     "isNiche": False
#   },
#   {
#     "category": "Film & TV",
#     "id": "622a1c347cc59eab6f94fbf5",
#     "correctAnswer": "\"Cinderella story. Outta nowhere. A former greenskeeper, now, about to become the Masters champion. It looks like a mirac...It's in the hole! It's in the hole! It's in the hole!\"",
#     "incorrectAnswers": [
#       "\"As God is my witness, I'll never be hungry again.\"",
#       "\"Open the pod bay doors, please, HAL.\"",
#       "\"Oh, Jerry, don't let's ask for the moon. We have the stars.\""
#     ],
#     "question": "Which of these quotes is from the film 'Caddyshack'?",
#     "tags": [
#       "quotes",
#       "film",
#       "film_and_tv"
#     ],
#     "type": "Multiple Choice",
#     "difficulty": "hard",
#     "regions": [],
#     "isNiche": False
#   },
#   {
#     "category": "Film & TV",
#     "id": "622a1c377cc59eab6f9505e4",
#     "correctAnswer": "Kenneth Branagh",
#     "incorrectAnswers": [
#       "Michael Ironside",
#       "Luke Evans",
#       "Tom Waits"
#     ],
#     "question": "Which actor has featured in films including Harry Potter and the Chamber of Secrets and Dunkirk?",
#     "tags": [
#       "acting",
#       "film",
#       "film_and_tv"
#     ],
#     "type": "Multiple Choice",
#     "difficulty": "hard",
#     "regions": [],
#     "isNiche": False
#   },
#   {
#     "category": "Film & TV",
#     "id": "622a1c377cc59eab6f950786",
#     "correctAnswer": "Ben Affleck",
#     "incorrectAnswers": [
#       "Keanu Reeves",
#       "Donald Sutherland",
#       "Christian Bale"
#     ],
#     "question": "Which actor played the role of Batman in Batman v Superman: Dawn of Justice and Justice League?",
#     "tags": [
#       "actors",
#       "film",
#       "dc",
#       "comics",
#       "film_and_tv",
#       "batman"
#     ],
#     "type": "Multiple Choice",
#     "difficulty": "hard",
#     "regions": [],
#     "isNiche": False
#   },
#   {
#     "category": "Film & TV",
#     "id": "622a1c377cc59eab6f95067f",
#     "correctAnswer": "Paul Newman",
#     "incorrectAnswers": [
#       "Tim Roth",
#       "Hugo Weaving",
#       "Warwick Davis"
#     ],
#     "question": "Which actor has featued in films including The Sting and The Towering Inferno?",
#     "tags": [
#       "acting",
#       "film_and_tv"
#     ],
#     "type": "Multiple Choice",
#     "difficulty": "hard",
#     "regions": [],
#     "isNiche": False
#   },
#   {
#     "category": "Film & TV",
#     "id": "625fd672dc0dd3b72da64cf1",
#     "correctAnswer": "1975",
#     "incorrectAnswers": [
#       "1970",
#       "1980",
#       "1985"
#     ],
#     "question": "One Flew Over the Cuckoo's Nest was released in which year?",
#     "tags": [
#       "film",
#       "film_and_tv"
#     ],
#     "type": "Multiple Choice",
#     "difficulty": "hard",
#     "regions": [],
#     "isNiche": False
#   },
#   {
#     "category": "Film & TV",
#     "id": "622a1c377cc59eab6f950667",
#     "correctAnswer": "Warwick Davis",
#     "incorrectAnswers": [
#       "Timothy Spall",
#       "Jack Lemmon",
#       "Paul Newman"
#     ],
#     "question": "Which actor has featued in films including Rogue One and Return of the Jedi?",
#     "tags": [
#       "star_wars",
#       "film_and_tv"
#     ],
#     "type": "Multiple Choice",
#     "difficulty": "hard",
#     "regions": [],
#     "isNiche": False
#   }
# ]

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