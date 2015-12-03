# Mason-Rummy - Python
Rummy game implemented with Python

Background:

We will implement a brand new card game called Mason Rummy. It shares some common heritage with many other Rummy card games, but whether you are familiar with those other games or not, be sure to pay attention to the rules of our game. To make our program more useful, we will store long-term high scores in a file. 

 
Menu A: Main Menu
1. View scores
2. Play 2-player game 3. Play 3-player game
4. Play 2-player game with stacked deck 5. Play 3-player game with stacked deck 6. Quit

Menu B: Choose Player Type
1. new player
2. returning player

Menu C (example): Choose Previous Player
1. Ahmed 2. Bharat 3. Doris 4. …
 
Menu D: Which Card to Draw 1. Draw from stock pile
2. Draw from discard pile

Menu E: Next Action
1. Play down cards 2. Discard

Menu F (example): Select Cards
1. 4 Spade 2. 5 Spade 3. 10 Heart
4. 10 Patriot
5. A Diamond 6. …
 

Menu D: Which Card to Draw 1. Draw from stock pile
2. Draw from discard pile

Menu E: Next Action
1. Play down cards 2. Discard

Menu F (example): Select Cards
1. 4 Spade 2. 5 Spade 3. 10 Heart
4. 10 Patriot
5. A Diamond 6. …

Basic Game Concept (the gist of the game)
Mason Rummy is a rummy game played with a five-suit deck. The extra suit has the normal 13 cards, and the symbol is a green Patriot. The two or three Players start with ten cards each, and take turns drawing a card, playing melds or runs (until someone runs out of cards to end the round), and discarding. Cards left over at the end of a round in the other players' hands count against them; the second player goes first in the next round and so on. After three rounds, the game is over and the overall lowest score wins.

Main Program Flow
· Program user can choose a main menu option (menu A) – number of players, whether to use a shuffled deck or a "stacked" (pre-ordered) deck. (or view scores, or quit).
· If a stacked deck is indicated, immediately ask user for either a deck file's name or the word "no". If any issues arise (file not found, contents wrong), complain and ask again for a file name. If the user types "no", let them escape back to the main menu.
· For each player, choose (menu B) either a new player or returning player (from alphabetical numbered list – menu C).
· First player goes first; players take turns in order until someone wins the round. Cards remaining in a player's hand counts against them.
· There are always exactly three rounds in a game of Mason Rummy.
· The lowest score wins the entire game.
· Record or update for each player their number of wins/losses, and "best winning score". New players must be added to the scores. This file should be immediately updated.
· Re-visit main menu (menu A).

Game Flow
· A round starts by dealing ten cards a time to each player. (This is important – the first ten cards all go to player 1, next ten to player 2, and so on. After you've given each player their cards, you need to place the next card from the deck into the discard pile (so that the first player still has the choice of either a discarded card or a stock pile card). In real life we'd deal one at a time in a circle repeatedly, but we want our stacked decks to be easy to read, so the program must always behave in this described way).
· The players go in the order they were entered in the main menu.
· Each turn, a player can see the following:
o The "discard pile" (discarded cards, face-up, but only top one visible).
o Each player's already-laid-down cards in front of them (optional)
o Their own hand of cards
· To start taking a turn, the player must draw a card (menu D). They will select either the "stock pile" (receiving the top card from the stock pile of not-yet-used cards), or they will select the "discard pile" (receiving the face-up top card from the discard pile).
· After drawing a card, the player may repeatedly lay down cards if they choose:
o A "meld" (3 or more of a kind) can be laid down.
o A "run" (3 or more in a row, of the same suit) can be laid down.
o Individual cards can be laid down if they fit on that player's own existing meld or run. If a player chooses to lay down a card that happens to both fit in an existing meld, and also fits at the end of an existing run, we will assume that it always plays on the run.
→ Player indicates cards via menu F, and entering all numbers of cards to play separated by commas. (Just this time, you can use the eval function to get a tuple !)
→ Player is again given menu D menu E after each lay down.
· To finish the turn, the player discards a single card. If the player plays his or her last card either by laying it down or discarding it, the round is over.

Files
· The scores will always be stored in a file named "scores.csv".
· The scores.csv file is a csv file with four columns (in this order) for "name", "games won", "games lost", and "best score". Formatting: header row first, double quotes and commas.
· A .deck file should be a file filled with 65 card descriptions, separated by whitespace (spaces, tabs, or newlines). These can be used to make testing repeatable. Note: card descriptions are very specific; see that section  next in our specification. Putting ten cards on a line for the first three players is convenient, and should still be readable if you use the split() method to get the cards.

Card Descriptions
A card description (representation for .deck files) is always a 2-character sequence:
· The first character represents the value, or number of "pips": possible values are
1,2,3,4,5,6,7,8,9,T,J,Q,K,A. (we already have Ace! no 1)   (T for ten, J for Jack, Q for Queen, K for King, A for Ace).
· The second character represents the suit. Options: CDHSP. (Clubs, Diamonds, Hearts, Spades, Patriots).
· When we display a card during the program, we want to use this same representation. You may write out longer descriptions as well during menu options, such as "TP (ten of patriots)", if it helps.

Using Exceptions
Some conditions must be obeyed in implementing the game.
· You must use exceptions and try-except blocks effectively, so that every single menu selection only allows a valid choice to be made.
· Players can't lay down cards when the game's rules forbid it. (leave then in the player's hand).
· The high scores file might not exist. (If it did exist, though, you may assume it has the correct csv 
 
formatted data in it).
· A deck file might not exist. Ask again. (they can always type "no" to escape).
· A deck file might not have correct information in it – you must require that it has exactly 65 entries in it. Ask again. (they can always type "no" to escape).
Points
The numbered cards are worth the number (a 7H is worth 7, a 10C is worth 10, and so on). The "face cards" (Jack, Queen, King) are each worth ten points. An Ace is worth 15 points.

Class Usage:
Your program implementation must define – and use – the classes described below, must contain the specified instance variables (data), and must implement the specified methods.
1. Card
·	data: suit and value (some representation of CDHSP/123456789TJQKA)
·	behaviors: extends_run(..), card_point_value(..), __str__(..), __init__(..)
2. Hand – list of cards
·	data: list of cards
·	behaviors: hand_point_value(..), already_laid_down(..), __str__(..), __init__(..)
3. Player
·	data: hand of cards, current score (in this game), name
·	behaviors: take_turn (..), __str__(..), __init__(..)
4. ScoreTable
·	data: list of scores
·	behaviors: read_scores(..), save_scores(..), clear_scores(..) , __str__(..), __init__(..)

Requirements, Details, and Even More Notes
· A "meld" is three or more cards of the same value – e.g., three Kings, three 7's, three Aces, and so on.
· A "run" is three or more cards, in consecutive order, of the same suit – e.g., 3S, 4S, 5S; 9P,10P, JP.
· Aces are always high.
· Only the specified menus should be used, and always with options in the order listed. There are other times we ask for a specific piece of information (deck file name, player name, et cetera), but your
program must be able to run on the exact same test files as everyone else's. We will provide a sample deck file and inputs when we get the chance.
· A player name must not be the empty string.
· Don't forget you can feed inputs rather than manually typing them (see project 4 for more info).
· You can implement the exceptions entirely after everything else if you're not ready for that part yet.
· Pay close attention to the requirements and grading rubric – while any program that can be written in an object oriented style can also be written as a plain procedural program, you need to use object oriented principles to get full credit on this assignment, because that is one of the main goals of this assignment.
· Users always type file extensions when they type file names (e.g., "stacked_test1.deck").
· All files are assumed to be in the same directory as where you execute the Python program.
· You can make as many extra functions or methods as you want in creating your solution.
· You can use any methods/functions discussed in class. If you want to use any other modules (beyond clearing the screen), you must get permission first.
· If the stock pile runs out, remove the top-card from the discard pile, reverse its order, and use these old cards from the discard pile as the new stock pile. The oldest card from the discard pile will be the first drawn card of the replenished stock pile.




 

 

 

 


Additional Notes!
· Although it might seem silly since we all look at the same screen, every player of the game is a human.
So one player sits down, takes their turn, and then trades seats with the next player to take their turn, and so on. The "clear the screen" extra credit is supposed to make the game a bit more realistic, but unless you' attempt the "AI" extra credit, you don't need to implement any sort of computer-player.
· You can always add more things to your implementation: more classes, more methods, more functions, more parameters to any method/function, more instance variables to your class definitions, and so on. While we need your menu structure to match the description from the user's perspective, the internals of your solution should largely be up to you.
· The ordering of scores when you print them out doesn't matter, as long as each row is correct and all entries from the file show up once (so, if you use a dictionary somehow the ordering of the results can be whatever happens; or if you use lists, the order in the file is also okay).
· If the user requests a stacked deck, just re-use the stacked deck each round. (Whether you re-open the file each round, or save a copy somewhere, it doesn't matter).
· A specific player can only be in the game once.
· You should import the random module, so that you can use the shuffle function from it. Whenever you need to shuffle the deck (just for starting new games that don't use a stacked deck), you just call
random.shuffle(list_of_cards), where your deck is the list_of_cards.
· The "top" of a deck, if you are using a list, is the zero-indexed item. So if you are putting a card on top, you need to append it to the 'front'. If you want to take a card out of the list, you will pop from the front as well.  (Note that this means the first card in a .deck file will be at position 0, and it will then be the first card dealt to the first player... it all works together well).
· because we use "A" to represent an ace, there is no "1" card. The possible values are 2,3,4,5,6,7,8,9,T,J,Q,K,A.
· The clear_scores() method isn't needed any more. I'd wanted to have another main menu option to empty out the scores, but removed it to make the project a bit smaller and forgot to remove this option as well.


Extra stuff to implement: 
1.  Create an artificial intelligence player. Give a player the name "AI" to initiate. This means you could have multiple AI's playing at once! (Please add AI to the scores file, like all other players).
a.   Must select top card from discard pile if it completes a new run/meld or can be laid down on an existing meld/run; otherwise, chooses stock pile.
b.   Must play existing runs first, then existing melds, then allowed singleton cards. Always plays playable cards (no holding out until it can play all at once, which is an interesting but risky strategy in rummy games).
c.   correctly use inheritance to have both a pc_player class be a subclass of the player class, and also a live_player class be a subclass of the player class.
2. use clear-screen effectively – try to have things stay stationary on screen from turn to turn!
3. use a custom exception class to signal that the current round is over (as opposed to using 'normal' control flow choices like loops, if-elses, and breaks/continues).
4. 
Clearing the Screen
We can actually "clear" the screen by having the terminal window scroll upwards sufficiently. If you include the following import statement and function definition, you can then just call clear_screen() whenever you want to clear the screen.

import8os8 8
def8clear_screen():8
8888if8os.name8==8"posix":8 88888888clear_cmd8=8"clear"8 8888elif8os.name8==8"nt":8 88888888clear_cmd8=8"cls"8 8888else:8
88888888raise8Exception8("\n\n\n***8Unsupported8System8***\nApplication8Terminating8!!!\n\n\n")8 8888os.system(clear_cmd)8


