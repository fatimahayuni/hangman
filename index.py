"""
The goal of this project is to give you practice with lists, loops, and logic.

You will re-create the classic game of HangMan, with a twist...

You will create a list of words or phrases. These will be hard-coded in your Python code.

Your game will begin by choosing one of the words or phrases from your list.

The user will be presented with the chosen item but the letters will be starred out. For example, if the word chosen from the list was "Over The Rainbow", 
then the word presented to the player at the start will be "**** *** *******".

The player will be asked to input a letter (characters between a-z). Capital letters should not affect the logic, so 'A' is equivalent to 'a'.

Numbers, symbols, and more than 1 input character is not valid input. This should prompt the user to re-enter the desired letter if this occurrs.

If the letter exists in the current word/phrase, then the letters should be revealed. So, if I was to input "t" for the "Over The Rainbow" phrase, then the phrase presented to the player will now be "**** T** *******".

After guessing, the user will be prompted with "tries remaining". For each phrase or word in the list, there should be an associated maximum number of tries to guess it. 

For example, "Over The Rainbow" is more difficult then guessing "Apple", so "Over The Rainbow" should give the player (for example) 8 tries, but "Apple" only 5 tries.

You can pick how much tries should be allowed for each word or phrase that you use.

You will need to consider how you associate the maximum number of tries with the words/phrases.

If the player doesn't guess the word/phrase within the maximum number of tries, they fail.

The program will ask the user if they would like to play again. A "Yes" respone will start the game again, but a "No" type response should exit the program.

Your program should be entirely function based, so the start of the program should be this:

def main():
	# Code goes here
	pass

main()
"""