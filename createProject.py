import random
import tkinter as tk
def choose_word():
    words = {"python": "Python is a powerful programming language used in cybersecurity, AI, and web development.",
             "computer": "Computers are the backbone of modern technology, impacting fields like cybersecurity and automation.",
             "program": "Programming allows us to create software, solve problems, and secure digital systems.",
             "developer": "Developers build software that drives innovation, including security tools and AI applications.",
             "algorithm": "Algorithms power everything from search engines to encryption, making digital security possible."}
    word = random.choice(list(words.keys()))
    return word, words[word]

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def draw_hangman(canvas, attempts):
    canvas.delete("all")
    canvas.create_line(20, 180, 120, 180, width=5)
    canvas.create_line(70, 180, 70, 20, width=5)
    canvas.create_line(70, 20, 150, 20, width=5)
    canvas.create_line(150, 20, 150, 50, width=5)
    
    if attempts <= 5:
        canvas.create_oval(130, 50, 170, 90, width=3)  # Head
    if attempts <= 4:
        canvas.create_line(150, 90, 150, 140, width=3)  # Body
    if attempts <= 3:
        canvas.create_line(150, 100, 130, 120, width=3)  # Left Arm
    if attempts <= 2:
        canvas.create_line(150, 100, 170, 120, width=3)  # Right Arm
    if attempts <= 1:
        canvas.create_line(150, 140, 130, 170, width=3)  # Left Leg
    if attempts == 0:
        canvas.create_line(150, 140, 170, 170, width=3)  # Right Leg

def update_display():
    word_display.config(text=display_word(word, guessed_letters))
    attempts_display.config(text=f"Attempts left: {attempts}")
    draw_hangman(canvas, attempts)

def guess_letter():
    global attempts, guessed_letters
    guess = guess_entry.get().lower()
    guess_entry.delete(0, tk.END)
    
    if len(guess) > 1:  # Full word guess
        if guess == word:
            guessed_letters = list(word)  # Reveal entire word
            result_display.config(text=f"Congratulations! You guessed the word: {word}")
            fact_display.config(text=f"Did you know? {fact}")
            guess_button.config(state=tk.DISABLED)
        else:
            result_display.config(text="Incorrect word guess!")
            attempts -= 1
    else:  # Single letter guess
        if guess in guessed_letters:
            result_display.config(text="You already guessed that letter.")
        elif guess in word:
            result_display.config(text="Good guess!")
            guessed_letters.append(guess)
        else:
            result_display.config(text="Incorrect letter guess!")
            guessed_letters.append(guess)
            attempts -= 1
    
    update_display()
    if set(guessed_letters) >= set(word):
        result_display.config(text=f"Congratulations! You guessed the word: {word}")
        fact_display.config(text=f"Did you know? {fact}")
        guess_button.config(state=tk.DISABLED)
    elif attempts == 0:
        result_display.config(text=f"Game over! The word was: {word}")
        guess_button.config(state=tk.DISABLED)

# Initialize game
word, fact = choose_word()
guessed_letters = []
attempts = 6

# Set up GUI
root = tk.Tk()
root.title("Hangman Game")
canvas = tk.Canvas(root, width=200, height=200)
canvas.pack()

draw_hangman(canvas, attempts)
word_display = tk.Label(root, text=display_word(word, guessed_letters), font=("Arial", 16))
word_display.pack()

attempts_display = tk.Label(root, text=f"Attempts left: {attempts}", font=("Arial", 12))
attempts_display.pack()

result_display = tk.Label(root, text="", font=("Arial", 12))
result_display.pack()

fact_display = tk.Label(root, text="", font=("Arial", 12), wraplength=300, justify="center")
fact_display.pack()

guess_entry = tk.Entry(root)
guess_entry.pack()

guess_button = tk.Button(root, text="Guess", command=guess_letter)
guess_button.pack()

root.mainloop()