# 🎙️ VANI – Voice-Activated Natural Intelligence Assistant

> A Python-based voice assistant with Wikipedia integration, Indian-English TTS, and system controls — built from scratch.

---

## 📌 What is VANI?

**VANI** (Voice-Activated Natural Intelligence) is a personal desktop voice assistant built using Python. It listens to voice commands, responds with a natural Indian-English accent, and answers general knowledge questions using Wikipedia — all in real time.

The name *Vani*  means *speech* or *voice* in Hindi — fitting for my first voice assistant.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🗣️ Voice Recognition | Listens via microphone using Google Speech API |
| 🔊 Text-to-Speech | Speaks back in Indian-English accent (gTTS) |
| 📖 Wikipedia Search | Answers "who is / what is" questions live |
| ⏰ Time Awareness | Greets user based on time of day |
| 🌐 Browser Control | Opens Google, YouTube via voice |
| 🖥️ App Launcher | Opens Notepad, Calculator via voice |
| 🎭 Context-Aware Intro | Different intro for teacher vs general user |
| ❌ Graceful Exit | Recognizes multiple goodbye phrases |

---

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Speech Input:** `SpeechRecognition` + Google Speech API
- **Voice Output:** `gTTS` + `playsound`
- **Knowledge Base:** `wikipedia-api`
- **System Control:** `os`, `webbrowser`, `datetime`

---

## 📁 Project Structure

```
VANI-Assistant/
│
├── vani.py             # Main assistant script
├── requirements.txt    # All dependencies
├── SETUP.md            # Step-by-step setup guide
└── README.md           # This file
```

---

## ⚙️ Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/utkarsh-buildspark/VANI-Assistant.git
cd VANI-Assistant

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run VANI
python vani.py
```

> See **SETUP.md** for detailed installation help and error fixes.

---

## 🎤 Voice Commands

```
"What is the time"        → Tells current time
"Open Google"             → Opens google.com
"Open YouTube"            → Opens youtube.com
"Open Notepad"            → Launches Notepad
"Open Calculator"         → Launches Calculator
"Who is [person]"         → Wikipedia search
"What is [topic]"         → Wikipedia search
"Tell me about [topic]"   → Wikipedia search
"Introduce yourself"      → VANI introduces herself
"Goodbye / Bye / Exit"    → Shuts down
```

---

## 🔄 How It Works

```
Microphone Input
      ↓
SpeechRecognition (Google API)
      ↓
Command Parser
      ↓
┌──────────────────────────────┐
│  Known Command?              │
│  YES → Execute directly      │
│  NO  → Wikipedia API Search  │
└──────────────────────────────┘
      ↓
gTTS converts response to speech
      ↓
playsound plays the audio
```

---

## 👨‍💻 Author

**Utkarsh**

🔗 [LinkedIn](https://www.linkedin.com/in/utkarsh-buildspark)
🌐 [Portfolio](https://build-spark.netlify.app)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
