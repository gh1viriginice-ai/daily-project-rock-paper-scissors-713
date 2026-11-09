#!/usr/bin/env python3
import random

CHOICES = ["rock", "paper", "scissors"]
WINS = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

def play():
    player = input("Rock/Paper/Scissors? ").lower().strip()
    if player not in CHOICES:
        print("Invalid choice!"); return
    computer = random.choice(CHOICES)
    print(f"You: {player} | Computer: {computer}")
    if player == computer:
        print("Draw!")
    elif WINS[player] == computer:
        print("You win!")
    else:
        print("Computer wins!")

if __name__ == "__main__":
    play()
