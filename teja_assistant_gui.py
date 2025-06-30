<<<<<<< HEAD
import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pyttsx3
import speech_recognition as sr
import webbrowser
import pyjokes
import random

from openai import OpenAI

# Initialize TTS
engine = pyttsx3.init()
engine.setProperty("rate", 150)

# OpenAI API key
client = OpenAI(api_key="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")

# Functions
def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        status_label.config(text="Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio, language='en-IN')
            status_label.config(text=f"You said: {command}")
            return command.lower()
        except:
            status_label.config(text="Could not understand.")
            return ""

def play_music():
    music_folder = "music"
    if os.path.exists(music_folder):
        songs = [song for song in os.listdir(music_folder) if song.endswith(".mp3")]
        if songs:
            song_path = os.path.join(music_folder, random.choice(songs))
            os.startfile(song_path)
            speak("Playing music from your collection.")
        else:
            speak("No songs found. Opening YouTube.")
            webbrowser.open("https://www.youtube.com/results?search_query=play+music")
    else:
        speak("Music folder not found. Opening YouTube.")
        webbrowser.open("https://www.youtube.com/results?search_query=play+music")

def chat_with_gpt(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        reply = response.choices[0].message.content.strip()
        speak(reply)
        messagebox.showinfo("Teja says", reply)
    except Exception as e:
        speak("Sorry, I couldn't reach ChatGPT.")
        print(e)

def execute_command(command):
    if "youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube.")
    elif "google" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google.")
    elif "music" in command:
        play_music()
    elif "joke" in command:
        joke = pyjokes.get_joke()
        speak(joke)
    elif "chat" in command or "question" in command:
        speak("What do you want to ask?")
        query = listen()
        if query:
            chat_with_gpt(query)
    elif "exit" in command:
        speak("Goodbye!")
        root.destroy()
    else:
        speak("Sorry, I don't recognize that command.")

def run_voice_command():
    command = listen()
    if command:
        execute_command(command)

def run_text_command():
    command = text_entry.get()
    if command:
        execute_command(command)
        text_entry.delete(0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("Teja - Voice Assistant")
root.geometry("450x600")
root.configure(bg="#f0f0f0")

# Load image
try:
    img = Image.open("teja.jpg")
    img = img.resize((150, 150))
    photo = ImageTk.PhotoImage(img)
    photo_label = tk.Label(root, image=photo, bg="#f0f0f0")
    photo_label.pack(pady=10)
except:
    tk.Label(root, text="Photo not found!", bg="#f0f0f0", fg="red").pack()

# Heading
tk.Label(root, text="Hi! I'm Teja 👋", font=("Helvetica", 18, "bold"), bg="#f0f0f0").pack()

# Entry
text_entry = tk.Entry(root, font=("Helvetica", 14))
text_entry.pack(pady=10)

# Buttons
tk.Button(root, text="Speak", command=run_voice_command, font=("Helvetica", 12), bg="#4CAF50", fg="white", width=15).pack(pady=5)
tk.Button(root, text="Submit Text", command=run_text_command, font=("Helvetica", 12), bg="#2196F3", fg="white", width=15).pack(pady=5)
tk.Button(root, text="Exit", command=root.quit, font=("Helvetica", 12), bg="#f44336", fg="white", width=15).pack(pady=5)

# Status Label
status_label = tk.Label(root, text="", font=("Helvetica", 10), bg="#f0f0f0")
status_label.pack(pady=10)

root.mainloop()
=======
import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pyttsx3
import speech_recognition as sr
import webbrowser
import openai
import random

# Initialize TTS
engine = pyttsx3.init()
engine.setProperty("rate", 150)

# OpenAI API key
openai.api_key = "sk-proj-kEwtVV6XZCFvU1TA"

# Functions
def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        status_label.config(text="Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio, language='en-IN')
            status_label.config(text=f"You said: {command}")
            return command.lower()
        except:
            status_label.config(text="Could not understand.")
            return ""

def play_music():
    music_folder = "music"
    if os.path.exists(music_folder):
        songs = [song for song in os.listdir(music_folder) if song.endswith(".mp3")]
        if songs:
            song_path = os.path.join(music_folder, random.choice(songs))
            os.startfile(song_path)
            speak("Playing music from your collection.")
        else:
            speak("No songs found. Opening YouTube.")
            webbrowser.open("https://www.youtube.com/results?search_query=play+music")
    else:
        speak("Music folder not found. Opening YouTube.")
        webbrowser.open("https://www.youtube.com/results?search_query=play+music")

def chat_with_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        answer = response.choices[0].message["content"].strip()
        speak(answer)
        messagebox.showinfo("Teja says", answer)
    except Exception as e:
        speak("Sorry, I couldn't reach ChatGPT.")
        print(e)

def execute_command(command):
    if "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube.")
    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google.")
    elif "play music" in command:
        play_music()
    elif "chat" in command or "question" in command:
        speak("What do you want to ask?")
        query = listen()
        if query:
            chat_with_gpt(query)
    elif "exit" in command:
        speak("Goodbye!")
        root.destroy()
    else:
        speak("Sorry, I don't recognize that command.")

def run_voice_command():
    command = listen()
    if command:
        execute_command(command)

def run_text_command():
    command = text_entry.get()
    if command:
        execute_command(command)
        text_entry.delete(0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("Teja - Voice Assistant")
root.geometry("450x600")
root.configure(bg="#f0f0f0")

# Load image
try:
    img = Image.open("teja.jpg")
    img = img.resize((150, 150))
    photo = ImageTk.PhotoImage(img)
    photo_label = tk.Label(root, image=photo, bg="#f0f0f0")
    photo_label.pack(pady=10)
except:
    tk.Label(root, text="Photo not found!", bg="#f0f0f0", fg="red").pack()

# Heading
tk.Label(root, text="Hi! I'm Teja 👋", font=("Helvetica", 18, "bold"), bg="#f0f0f0").pack()

# Entry
text_entry = tk.Entry(root, font=("Helvetica", 14))
text_entry.pack(pady=10)

# Buttons
tk.Button(root, text="Speak", command=run_voice_command, font=("Helvetica", 12), bg="#4CAF50", fg="white", width=15).pack(pady=5)
tk.Button(root, text="Submit Text", command=run_text_command, font=("Helvetica", 12), bg="#2196F3", fg="white", width=15).pack(pady=5)
tk.Button(root, text="Exit", command=root.quit, font=("Helvetica", 12), bg="#f44336", fg="white", width=15).pack(pady=5)

# Status Label
status_label = tk.Label(root, text="", font=("Helvetica", 10), bg="#f0f0f0")
status_label.pack(pady=10)

root.mainloop()
>>>>>>> cb815d330d32ae9627ca4ccafd43b5b5d81d8a4f
