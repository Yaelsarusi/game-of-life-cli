# What is game of life?
Read the first and second sections in the Wikipedia article:
https://en.wikipedia.org/wiki/Conway's_Game_of_Life

## Your task
Create a python script called gameoflife.py simulating the game of life and
printing it to the shell.

## The script accepts two command line arguments:
state_file_path
Path to a file containing the initial state for the simulation. You may choose
the format of the file.
generations
The number of generations to run the simulation.

For example:

```bash-3.2$ python gameoflife.py ~/initial_state.txt 1000```

Will run the simulation 1000 generations, starting with the state encoded in
initial_state.txt

## Notes:
Print the new state every 100ms
Each time you print the new state, it should override the previous output in
the shell so as to create an animation.

## Example Output
This is the last output of the script for some 7x3 board. "*" signifies living cells.

bash-3.2$ python gameoflife.py ~/initial_state.txt 1000

| *** **|
| **  * |
|       |

bash-3.2$
