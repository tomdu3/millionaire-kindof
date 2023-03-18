![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Who Wants To Be A Millionaire Kind Of
![Am I Responsive Image](./assets/readme_files/amiresponsive.png)

[View the live project here](https://millionaire-kindof.herokuapp.com/)
## Table of contents
1. [Introduction](#Introduction)
2. [UX](#UX)
    1. [Ideal User Demographic](#Ideal-User-Demographic)
    2. [User Stories](#User-Stories)
    3. [Development Planes](#Development-Planes)
    4. [Design](#Design)
3. [Features](#Features)
    1. [Design Features](#Design-Features)
    2. [Existing Features](#Existing-Features)
    3. [Features to Implement in the future](#Features-to-Implement-in-the-future)
4. [Issues and Bugs](#Issues-and-Bugs)
5. [Technologies Used](#Technologies-Used)
     1. [Main Languages Used](#Main-Languages-Used)
     2. [Libraries And Modules Used](#Libraries-And-Modules-Used)
     3. [Frameworks And Programs Used](#Frameworks-And-Software-Used)
6. [Testing](#Testing)
     1. [Testing.md](TESTING.md)
7. [Deployment](#Deployment)
     1. [Deploying on Herokus](#Deploying-On-Heroku)
8. [Credits](#Credits)
     1. [Media](#Media)
     2. [Code](#Code)
9. [Acknowledgements](#Acknowledgements)
***

## Introduction
The game Who Wants To Be A Millionaire Kind Of is the 3rd Portfolio Project at the Code Institute. It is an hommage to the famous TV game that conquered the world. In this version, the questions are related to the movies.

The purpose of this project is to build a command-line application that allows the user to manage a common dataset about a particular domain.

[Back to top ⇧](#Who-Wants-To-Be-A-Millionaire-Kind-Of)

## UX
### Ideal User Demographic
There are two types of ideal users:
* New User
* Current User

### User-Stories
#### New User Goals
* As a new user, I want easily navigate through the application.
* As a new user, I want easily consult and find the rules.
* As a new user, I want to test my knowledge about the movies.
* As a new user, I want to have learn something while having fun.


#### Current User Goals
* As a current user, I want a game similar to the Who Wants To Be A Millionaire TV game.
* As a frequent user, I want to test my knowledge about the movies.
* As a frequent user, I want have questions with a progressive difficulty.
* As a frequent user, I want to improve my knowledge and score.

[Back to top ⇧](#Who-Wants-To-Be-A-Millionaire-Kind-Of)

### Development-Planes
To build a command-line application to give the user an experience similar to the one of the Who Wants To Be A Millionaire TV game, with the questions about movies.

#### Strategy
Strategy incorporates user needs as well as product objectives. This application will focus on the following target audience, divided into three main categories
* Audience
    * New Users
    * Current Users

* Demographic
    * All ages

* Psychographic:
    * Movie fan
    * Quiz fan
    * Problem solver

The application is supposed to enable the user to:
* Play the Who Wants To Be A Millionaire
* Insert a player name
* Answer to a series of randomly selected questions from the database
* Experience a progressive difficulty level
* Be aware of the points gained, threshold points and won points
* Know when answers wrongly and learn the correct answer
* Enter the high score databes if there are some points won at the game end
* Restart the game if wanted with a new set of questions
* Read the instructions about the game
* See the high scores from the database

The Developer/Administrator needs to receive:
    * Player's Name

#### Scope

After defining goals of the game, we are delineating the necessary features:
* Required functionalities
    * Intro screen display
    * Question database loader
    * How to play the game instructions display
    * High scores display
    * Global Menu
    * Quiz starter
    * Quiz questions generator
    * Points/Threshold display
    * Question display and guess
    * Answer validator
    * Correct answer displayed if wrongly answered or congratulatory message if answered correctly
    * On game end - displayed a new screen with appropriate messages, points and the high scores saved to Google Sheet
    * On application exit - displayed a new screen with Thank you note


#### Structure
A flowchart made in [LUCID](https://lucid.app.com/ "Link to Lucid") demonstrates the game's structure.

<details>
<summary>Flowchart Image</summary>

![Flowchart](./assets/readme_files/flowchart.svg)

</details>

#### Skeleton
Being the game in fact a terminal application, the skeleton plane would be somwhat in between the presented flowchart and the design. Therefore, the relative details will follow in the next section. 

[Back to top ⇧](#Who-Wants-To-Be-A-Millionaire-Kind-Of)

### Design
The overall design of this command line application is quite simple. The developer at first decided to use different colours and ASCII text art. But, upon the deployment on Heroku, and some feedback from the testers, the developer opted for a more simpler design and less colourful in order to keep the best possible visibility of the application - beign a quiz game based on a lot of text that needs to be read.

For more engaging design, the devlopper has decided use a few screens at the intro, end game, end quiz, display high scores, etc. ASCII art is used for a games 'LOGO' that repeat itself throughout the application. For the passages from the screens, the developer opted for a simple keypress detection.

The interactive parts of the application are the user name insertion, the menu and the answering to the questions, which require a valid input and pressing of the 'Enter' key.

[Back to top ⇧](#Who-Wants-To-Be-A-Millionaire-Kind-Of)

