# Import Statements
import sys
from random import choice
from customtkinter import *


# List of Words
words: list[str] = [
  "Python", "Java", "Rust", "Ruby", "HTML", "JavaScript", "MySQL",
  "Postgres", "MongoDB", "GitHub", "Linux", "Windows", "Android", "Apple", "Microsoft", "Google",
  "Amazon", "Tree", "Graph", "Hashmap", "Algorithm", "Pixel", "Compiler", "Debug", "Terminal",
  "PowerShell", "Binary", "Logic", "Internet", "Website", "Hosting", "Cloud", "Docker",
  "Eclipse", "VSCode", "PyCharm", "IntelliJ", "Tkinter", "Pygame", "Unity", "Arduino", "Scratch", "Gaming",
  "Patch", "ChatGPT", "YouTube", "Robotics", "Command", "Framework", "Library", "Input", "Megabyte", "Kilobyte",
  "Gigabyte", "Inheritance", "Processor", "Graphics", "Linux", "iOS", "macOS", "Swift", "Kotlin", "Argument",
  "Integer", "Conditional", "Loops", "Constant", "Event", "Iteration", "Syntax", "Exception", "Error",
  "StackOverflow", "Server", "Client", "Boolean", "String", "Array", "Queue", "Stack", "NoSQL", "Netflix",
  "Nvidia", "Tuple", "Sets", "JSON", "Data", "Memory", "Megahertz", "Chip", "Card", "Hertz",
  "BiOS", "Motherboard", "Monitor", "Keyboard", "Resolution", "Deepseek", "Grok", "Humanoid", "Level", "Digital",
  "Digit", "Octal", "Decimal", "Encrypt", "Swap", "Copy", "Paste", "Decrypt", "Secret", "Request", "Video",
  "Mixing", "Conversion", "Editing", "Intel", "Micro", "Macro", "Excel", "Wrap", "Display"
]

# Initial Variables
score = 0
guesses = 0
colors = ["#C8B653",
          "#538D4E", "#3A3A3C"]

# Declaring root
root = CTk()
root.title("")
root.geometry("800x650")

# Increment
increment = 0

# Title
main_label = CTkLabel(root, text="ProGrammar", font=("Britannic Bold", 120))
main_label.place(relx=0.5, rely=0.15, anchor="center")

# "Word' and Entry
choice_word = choice(words)
input_entry = CTkEntry(root, width=700, font=("Britannic Bold", 40), corner_radius=5, border_width=5,
                       border_color="white", height=40)
input_entry.place(relx=0.5, rely=0.3, anchor="center")

# Scores
scores = CTkLabel(root, text=f"Score: {0}", font=("Britannic Bold", 20))
scores.place(relx=0.075, rely=0.95, anchor="center")

def _check(word):
    global choice_word, colors,\
        increment, guesses, scores, score, frames

    # Determine Colors
    cols = []
    for i in range(len(word)):
        if word[i].lower() == choice_word[i].lower():
            cols.append(colors[1])
        elif word[i].lower() in choice_word.lower():
            cols.append(colors[0])
        else:
            cols.append(colors[2])
    guesses += 1

    # Put them on the screen
    for i in range(len(word)):
        frame = CTkFrame(root, border_width=4, border_color="white",
                         fg_color=cols[i],
                         width=50, height=55)
        frame.place(
            x=425 - (len(choice_word) * 55) // 2 + i * 55,
            y=285+increment, anchor="center"
        )
        label = CTkLabel(frame, text=word[i].upper(),
                         font=("Britannic Bold", 40))
        label.place(relx=0.5, rely=0.5, anchor="center")
        labels.append(label)
        frames.append(frame)

    increment += 60

    # Success
    if cols == [colors[1] for i in word]:
        for i in frames:
            i.destroy()
        frames.clear()
        increment = 0
        score += (6 - guesses)
        guesses = 0
        choice_word = choice(words)
        scores.configure(text=f"Score: {score}")
        input_entry.insert(0, "You got it!!")
        root.after(3000, lambda: input_entry.delete(0, "end"))

        # Restarting
        for i in range(len(choice_word)):
            frame = CTkFrame(root, border_width=4, border_color="white",
                                 fg_color="#3A3A3C",
                                 width=50, height=50)
            frame.place(
                  x=425 - (len(choice_word) * 55) // 2 + i * 55,
                  y=285, anchor="center"
              )
            label = CTkLabel(frame, text="",
                                 font=("Britannic Bold", 40))
            label.place(relx=0.5, rely=0.5, anchor="center")
            labels.append(label)
            frames.append(frame)

    # Losing the game
    if guesses == 6:
        root.after(3000, lambda x: root.destroy())
        sys.exit()

    input_entry.delete(0, "end")

# Initial Level
labels = []
frames = []
for i in range(len(choice_word)):
    frame = CTkFrame(root, border_width=4, border_color="white",
                     fg_color="#3A3A3C",
                         width=50, height=50)
    frame.place(
            x=425 - (len(choice_word) * 55) // 2 + i * 55,
            y=285, anchor="center"
    )
    label = CTkLabel(frame, text="",
                         font=("Britannic Bold", 40))
    label.place(relx=0.5, rely=0.5, anchor="center")
    labels.append(label)
    frames.append(frame)

input_entry.bind("<Return>", lambda n: _check(input_entry.get()))

root.mainloop()
