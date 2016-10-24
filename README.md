# Background

This game is a simple project, made purely for fun and for the sake of making a game. It is also used as an education tool in learning Ruby and scripting languages in general.

While it is based on old text adventure games of old, like Zork, my focus wasn't so much on the 'adventure' as[ect, as it is on the 'puzzle'. So this is more of a puzzle game than anything else. In order to proceed throughout the game, you will have to solve the various puzzles through each room, hopefully each one becoming more difficult or involved than the last.]

I don't want to make this game too sophisticated. That being said, I do have plans to eventually beef up the framework of this game so that it is easily expandable with new parts.

# Dev notes /  Architecture

Each room has a state. during each state, there is only 1 command that can be successfully executed to proceed to the next state.
every room begins in state 1, being unvisited. after that, each romve moves to state 2, a visited state.

# Releases

## Part 1

Part 1 is currently in development.