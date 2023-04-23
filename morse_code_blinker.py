import tkinter as tk
import RPi.GPIO as GPIO
from tkinter import messagebox
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

MORSE_CODE = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
              'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
              'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
              'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
              'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
              'Z': '--..'}

root = tk.Tk()
root.title("Morse code blinker")
root.geometry("400x300")

# LABEL #
instructions_label = tk.Label(root, text="Enter a word (max 12 characters):")
instructions_label.pack()

# ENTRY BOX #
entry = tk.Entry(root, width=30)
entry.pack()

# FUNCTIONS #
def morse_code():
        word = entry.get().upper()
        if len(word) > 12:
                messagebox.showerror("Error", "Word exceeds max length of 12 characters.")
                return
        for char in word:
                if char == ' ': # space
                        time.sleep(2.1);
                elif not (char.isalpha() or char.isspace()): 
                        messagebox.showerror("Error", "Input contains non-alphabetic characters.")
                        return
                else:
                        morse_code = MORSE_CODE.get(char, '')
                        for symbol in morse_code:
                                if symbol == '.': # dot
                                        GPIO.output(17, GPIO.HIGH)
                                        time.sleep(0.3)
                                        GPIO.output(17, GPIO.LOW)
                                        time.sleep(0.3)
                                elif symbol == '-': # dash
                                        GPIO.output(17, GPIO.HIGH)
                                        time.sleep(0.9)
                                        GPIO.output(17, GPIO.LOW)
                                        time.sleep(0.9)

def close():
        GPIO.cleanup()
        root.destroy()


# BUTTONS #
blink_button = tk.Button(root, text="Blink", command = morse_code, bg = "green", height=1, width=24)
blink_button.pack()

exit_button = tk.Button(root, text="Exit", command = close, bg = "red", height=1, width=24)
exit_button.pack()

root.protocol("WM_DELETE_WINDOW", close) #exit cleanly
root.mainloop()
