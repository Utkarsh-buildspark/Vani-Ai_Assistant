# ⚙️ VANI – Setup Guide

Step-by-step instructions to run VANI on your Windows PC.

---

## ✅ Requirements

- Windows 10 / 11
- Python 3.8 or above → [Download here](https://www.python.org/downloads/)
- Working microphone
- Internet connection

---

## 📥 Step 1 — Download the Project

```bash
git clone https://github.com/utkarsh-buildspark/VANI-Assistant.git
cd VANI-Assistant
```

Or download ZIP from GitHub → Extract the folder.

---

## 📦 Step 2 — Install Dependencies

Open Command Prompt inside the project folder and run:

```bash
pip install speechrecognition
pip install gtts
pip install playsound==1.2.2
pip install wikipedia-api
pip install pyaudio
```

> ⚠️ **If PyAudio fails on Windows:**
> ```bash
> pip install pipwin
> pipwin install pyaudio
> ```

Or install everything at once:
```bash
pip install -r requirements.txt
```

---

## ▶️ Step 3 — Run VANI

```bash
python vani.py
```

You will see:
```
Wikipedia module loaded successfully.
Initializing Vani...
Vani: Good morning sir. I am Vani. How can I assist you today?
Listening...
```

---

## 🎤 Step 4 — Try These Commands

Speak clearly into your microphone:

```
"What is the time"
"Open YouTube"
"Open Google"
"Who is Elon Musk"
"What is Python"
"Open Notepad"
"Goodbye"
```

---

## ❌ Common Errors & Fixes

| Error | Fix |
|---|---|
| `playsound` not working | Use `pip install playsound==1.2.2` |
| PyAudio install fails | Use `pipwin install pyaudio` |
| `Could not understand audio` | Speak clearly, reduce background noise |
| `Google API Error` | Check internet connection |
| `No module named 'speech_recognition'` | Run `pip install speechrecognition` again |

---

## 📌 Notes

- Uses **Google Speech API** for voice recognition (internet required)
- TTS uses **gTTS** with Indian-English accent (`tld='co.in'`)
- Wikipedia search returns first 250 characters of page summary
