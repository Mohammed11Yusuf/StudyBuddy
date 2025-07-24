

 StudyBuddy – Flashcard Quiz App

A simple, terminal-based flashcard quiz application written entirely in Python.

Created as the **final project** for [CS50’s Introduction to Programming with Python](https://cs50.harvard.edu/python/2022/), **StudyBuddy** allows users to create flashcards, save them, and quiz themselves through the command line. It’s perfect for memorizing vocabulary, practicing definitions, or studying general knowledge topics.

---

  Features

-  Create your own flashcards
- Save flashcards to a file (`flashcards.json`)
- Take a quiz and get scored
- Randomized question order
-  View all saved flashcards
-  Simple, menu-driven interface

---

  Getting Started

Requirements

- Python 3.x
- No external libraries needed
- Running the Program

Clone or download the repository, then run:

```bash
python studybuddy.py


--- StudyBuddy Menu ---
1. Add flashcard
2. Take quiz
3. Show all flashcards
4. Save and exit


studybuddy/
│
├── studybuddy.py         # Main application
├── flashcards.json       # Flashcard data file (auto-created)
└── README.md             # This file

>>>>>Data Persistence<<<<<<
All flashcards are stored in a local flashcards.json file in the following format:

json
Copy
Edit
{
  "What is the capital of France?": "Paris",
  "2 + 2": "4"
}
This file is automatically read and updated by the program. You can also edit it manually if needed.


