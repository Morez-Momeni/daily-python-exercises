## Problem
Build a small terminal simulator that records every command the user types into a linked list, mimicking a shell history. The program supports three special commands:

- `-his`    → clear the screen and display the entire history.
- `-clear`  → clear the screen (and record the command in history).
- `-search` → ask for a command and return all indices where it appears in history.
- Any other input → stored in history as a normal command.

`Ctrl+C` exits the loop gracefully.

## My Solution

The program reuses the `Node` and `LinkedList` classes from the previous exercise. Each new command is wrapped in a `Node` and appended to the list. Special commands trigger additional behaviour (clearing the screen, printing history, or searching).