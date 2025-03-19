#!/usr/bin/env python3
"""
true_false.py - A simple True/False quiz game.

Author: Carlos Valerio (CarlosValerioM)
Date: 2025/03/019
License: MIT
Dependencies: None (built-in functions only)

Description:
This script runs a quiz game where the user answers True or False questions.
It takes a list of questions and their corresponding correct answers.
The user is prompted with each question, and their responses are evaluated.

The script then calculates the total score and displays the result at the end.

Usage:
Run the script and follow the prompts:
    python true_false.py

Example Output:
    Q.1: The Great Wall of China is visible from space. (True/False): False
    Your current score is 1/1
    Q.2: Water boils at 100 degrees Celsius at sea level. (True/False): True
    Your current score is 2/2
    ...
    Final Score: 5/5
"""
import random
from question import Question  # Import the Question class
from data import data  # Import the question data

def main():
    # Initialize the list that will hold all the questions
    question_bank = []
    score = 0  # Initialize the score counter
    question_number = 1  # Initialize the question number

    # Populate the question bank with Question objects from the data
    for line in data:
        question, answer = line.values()  # Extract question and answer from each entry in data
        question_bank.append(Question(question, answer))  # Add each question to the bank

    # Loop until the question bank is empty
    while question_bank:
        current_question = random.choice(question_bank)  # Randomly choose a question from the bank
        question_bank.remove(current_question)  # Remove the chosen question from the bank

        # Ask the user for their answer
        answer = input(f"Q.{question_number}: {current_question.text} (True/False): ")

        # Check if the answer is correct and update the score
        # `eval()` converts the input string to a boolean (True/False)
        # If the answer matches the correct answer, increment the score
        score += 1 if (eval(answer.capitalize()) == current_question.answer) else 0

        # Print the user's current score
        print(f"Your current score is {score}/{question_number}")

        # Increment the question number
        question_number += 1

    # End of the game, print final score
    print(f"Game Over! Your final score is {score}/{question_number - 1}")

# Check if the script is being run directly, and if so, execute the main function
if __name__ == '__main__':
    main()