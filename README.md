# 🤖 Teja Voice Assistant GUI

Teja is a personal voice-controlled desktop assistant built using Python and Tkinter. It responds to voice or typed commands, performs actions like opening websites, playing music, and answering questions using ChatGPT.

---

## 🎯 Features

- 🎤 Voice recognition and speech output
- 🧠 ChatGPT integration for smart Q&A
- 🎶 Play music from local folder or YouTube
- 🌐 Opens websites like Google and YouTube
- 🖼️ Custom GUI with your name, photo, and intro music
- 🧪 "Hey Teja" wake word supported

## 📁 Folder Structure

Voice-Command-Assistant/
├── teja_assistant_gui.py # Main Python GUI app
├── intro.mp3 # Intro music (optional)
├── teja.jpg # Display photo
├── README.md # This file
├── requirements.txt # Python dependencies
└── assets/ # (Optional) Extra files like icons or screenshots
## You can speak or type a command like:

- open google
- play music
- who is Virat Kohli
- chat: tell me a joke

## 🛠️ Requirements

- Python 3.9–3.12
- Internet connection (for ChatGPT & websites)

### Install required libraries:

```bash
pip install pyttsx3 speechrecognition wikipedia pywhatkit openai pillow

pip install playsound==1.2.2
