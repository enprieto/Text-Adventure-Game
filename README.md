# Background

This game is a simple project, made purely for fun and for the sake of making a game. It is also used as an education tool in learning Ruby and scripting languages in general.

While it is based on old text adventure games of old, like Zork, my focus wasn't so much on the 'adventure' aspect, as it is on the 'puzzle'. So this is more of a puzzle game than anything else. In order to proceed throughout the game, you will have to solve the various puzzles through each room, hopefully each one becoming more difficult or involved than the last.

I don't want to make this game too sophisticated. That being said, I do have plans to eventually beef up the framework of this game so that it is easily expandable with new parts.

# Dev notes /  Architecture

Each room has a state. during each state, only one command at a time can be successfully executed to proceed to the next state.
Every room begins in state 1, being unvisited. After that, each rome moves to state 2, a visited state, and progresses in states based on actions taken by the player.

# Releases

## Part 1

Part 1 is currently in development.

## python version

Python version of the game so far is now available