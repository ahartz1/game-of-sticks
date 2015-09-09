# Game of Sticks

#### System Requirements

* You will need to have **python&nbsp;3** installed on your machine or have access to a python&nbsp;3 interpreter. See [python's site](https://www.python.org/) for details.

* To run this program, save `sticks.py` to your computer. Using a command-line program (such as Terminal on Mac&nbsp;OS&nbsp;X), navigate to the folder containing the downloaded file and run the following line to play: `python3 sticks.py`

### Player vs. Player

**Game of Sticks – Player vs. Player** is a game where two players can play against each other. The game starts by choosing the number of sticks that will be in play (10–100). Each player takes 1–3 sticks per round. The player who takes the last stick is the loser. The two examples below demonstrate how the game should behave.

Example 1:

```
Welcome to the Game of Sticks!
How many sticks are there on the table initially (10-100)? 10

There are 10 sticks on the board.
Player 1: How many sticks do you take (1-3)? 3

There are 7 sticks on the board.
Player 2: How many sticks do you take (1-3)? 3

There are 4 sticks on the board.
Player 1: How many sticks do you take (1-3)? 3

There is 1 stick on the board.
Player 2: How many sticks do you take (1-3)? 1
Player 2, you lose.
```
Example 2:

```
Welcome to the Game of Sticks!
How many sticks are there on the table initially (10-100)? 500
Please enter a number between 10 and 100.
How many sticks are there on the table initially (10-100)? 3
Please enter a number between 10 and 100.
How many sticks are there on the table initially (10-100)? 50

There are 50 sticks on the board.
Player 1: How many sticks do you take (1-3)? 3

There are 47 sticks on the board.
Player 2: How many sticks do you take (1-3)? 55
Please enter a number between 1 and 3
Player 2: How many sticks do you take (1-3)? 3

There are 44 sticks on the board.
Player 1: How many sticks do you take (1-3)? 3
...

There is 1 stick on the board.
Player 1: How many sticks do you take (1-3)? 1
Player 1, you lose.
```

### Player vs. Learning AI without Training
**Game of Sticks – Player vs. Learning AI without Training** introduces an AI that learns as it goes. The gameplay is the same as with two human players, but as the AI learns, it will eventually become very, very good.
