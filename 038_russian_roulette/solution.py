"""
Problem #38: Russian Roulette Game
Date: 2026-09-03

A simple Russian roulette game where players take turns pulling the trigger.
The bullet is placed in one of 7 chambers. The player who gets the bullet loses.
"""

import random

PLAYER = []


def addUser():
    """Add players for the game."""
    player_numbers = int(input("Enter number of players: ").title())
    for u in range(player_numbers):
        player_name = input(f"Enter PlayerName[{u+1}]: ")
        PLAYER.append(player_name)


def gun():
    """Select a random chamber (1-7) for the bullet."""
    bullet = [1, 2, 3, 4, 5, 6, 7]
    gun_bullet = random.choice(bullet)
    return gun_bullet


def game():
    """Play the Russian roulette game."""
    bullet_number = gun()
    player_count = 0
    player_shot = 1

    while True:
        player = PLAYER[player_count]
        print(f"{player} shoots")
        if player_shot == bullet_number:
            print(f"{player} died!")
            break

        player_count += 1
        player_shot += 1

        if player_count > len(PLAYER) - 1:
            player_count = 0


def main():
    addUser()
    game()   


if __name__ == "__main__":
    main()