import json
import os
import random

DATA_FILE = "flashcards.json"

def load_deck():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return {}

def save_deck(deck):
    with open(DATA_FILE, "w") as file:
        json.dump(deck, file, indent=4)

def create_flashcard(deck):
    question = input("Enter the question: ")
    answer = input("Enter the answer: ")
    deck[question] = answer
    print("Flashcard added!")

def quiz(deck):
    if not deck:
        print("No flashcards available!")
        return
    questions = list(deck.items())
    random.shuffle(questions)
    score = 0
    for q, a in questions:
        user_answer = input(f"{q} > ")
        if user_answer.strip().lower() == a.strip().lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong. The correct answer is: {a}")
    print(f"Quiz complete! Score: {score}/{len(deck)}")

def menu():
    deck = load_deck()
    while True:
        print("\n--- StudyBuddy Menu ---")
        print("1. Add flashcard")
        print("2. Take quiz")
        print("3. Show all flashcards")
        print("4. Save and exit")
        choice = input("Choose an option: ")
        if choice == "1":
            create_flashcard(deck)
        elif choice == "2":
            quiz(deck)
        elif choice == "3":
            for q, a in deck.items():
                print(f"Q: {q} | A: {a}")
        elif choice == "4":
            save_deck(deck)
            print("Deck saved. Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    menu()
