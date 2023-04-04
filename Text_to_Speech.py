# Import the pyttsx3 library for text-to-speech conversion and the tkinter library for creating a GUI
import pyttsx3
import tkinter as tk

def speak():
    data = text_input.get()                   # Get the text entered in the GUI
    engine = pyttsx3.init()                   # Initialize the pyttsx3 engine for speech synthesis
    engine.say(data)                          # Use the engine to say the text and wait for it to finish
    engine.runAndWait()


## Gui Window:
root = tk.Tk()
root.title = ("Text - To - Speech App")

## Label and Input FIeld For user to Enter:
text_label = tk.Label(root, text = "Enter Text to Speak")
text_input = tk.Entry (root, width = 100)

## Speak button
speak_button = tk.Button(root, text = "Speak", command = speak)
quit_Button = tk.Button(root, text = "Exit", command = root.quit)

## Postioning the widgets:
text_label.grid(row=0, column=0, padx=5, pady=5)
text_input.grid(row=0, column=1, padx=5, pady=5)
speak_button.grid(row=1, column=1, padx=5, pady=5)
quit_Button.grid(row=2, column=1, padx=5, pady=5)

## Start GUI event loop
root.mainloop()