import speech_recognition as sr
import datetime
import os
import webbrowser
from gtts import gTTS
from playsound import playsound
import wikipediaapi  
try:
    wiki_wiki = wikipediaapi.Wikipedia(
        user_agent='VaniAssistant/1.0 (utkarsh@example.com)',
        language='en'
    )
    print("Wikipedia module loaded successfully.")
except Exception as e:
    print(f"Error loading Wikipedia module: {e}")

# --- (2) Speak Function ---

def speak(text):
    """Converts text to speech using gTTS, saves it as an mp3, and plays it."""
    print(f"Vani: {text}")
    try:
        tts = gTTS(text=text, lang='en', tld='co.in')
        filename = "speech.mp3"
        tts.save(filename)
        playsound(filename)
        os.remove(filename)
    except Exception as e:
        print(f"Speech error: {e}")

# --- (3) Greeting Function ---

def wish_me():
    """Greets the user based on the time of day."""
    hour = datetime.datetime.now().hour
    
    if 0 <= hour < 12:
        greeting = "Good morning sir."
    elif 12 <= hour < 18:
        greeting = "Good afternoon sir."
    else:
        greeting = "Good evening sir."
        
    speak(f"{greeting} I am Vani. How can I assist you today?")

# --- (4) Voice Input Function ---

def take_command():
    """Listens for voice input via microphone and returns it as text."""
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 
        r.adjust_for_ambient_noise(source, duration=1) 
        
        try:
            audio = r.listen(source, timeout=5)
        except sr.WaitTimeoutError:
            print("Listening timed out.")
            return "none"
        except Exception as e:
            print(f"Microphone error: {e}")
            return "none"

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query.lower()
    
    except sr.UnknownValueError:
        print("Could not understand audio")
        return "none" 
    except sr.RequestError as e:
        print(f"Google API Error: {e}")
        speak("Sir, please check your internet connection.")
        return "none"

# --- (5) Naya Function: Wikipedia se Poochein ---

def ask_wikipedia(query):
    """Searches Wikipedia for the query and returns the summary."""
    print(f"Searching Wikipedia for: {query}")
    try:
        # Wikipedia par page search karein
        page = wiki_wiki.page(query)
        
        if not page.exists():
            return f"Sorry sir, I could not find any information about {query} on Wikipedia."
        
        # Summary (pehli 2-3 line) ko chhota karein
        summary = page.summary[0:250] # Pehle 250 characters
        
        # Aakhri adhoore sentence ko hataayein
        if '.' in summary:
            summary = '.'.join(summary.split('.')[:-1]) + '.'
        
        return f"According to Wikipedia, {summary}"
        
    except Exception as e:
        print(f"Wikipedia Error: {e}")
        return "Sorry sir, I am having trouble connecting to Wikipedia right now."

# --- (6) Main Program Loop ---

if __name__ == "__main__":
    
    print("Initializing Vani...")
    wish_me()
    
    while True:
        try:
            query = take_command()

            if query == "none":
                continue

            # --- Command Logic ---

            # Aise 'who is' ya 'what is' waale sawaal bhi Wikipedia handle kar lega
            if "introduce yourself" in query:
                hour = datetime.datetime.now().hour
                if 0 <= hour < 12:
                    greeting = "Good morning"
                elif 12 <= hour < 18:
                    greeting = "Good afternoon"
                else:
                    greeting = "Good evening"

                if "teacher" in query:
                    today_date = datetime.datetime.now().strftime("%B %d, %Y")
                    speak(f"{greeting} mam. I am Vani, the auto-reply assistant created by my owner Utkarsh on 3rd november 2025. I can perform various operations and also reply to commands.")
                else:
                    speak(f"{greeting} sir. I am Vani. I was created by my owner Utkarsh for his personal assistance.")

            elif "what is the time" in query or "tell me the time" in query:
                str_time = datetime.datetime.now().strftime("%I:%M %p")
                speak(f"Sir, the time is {str_time}")

            elif "open notepad" in query:
                speak("Opening Notepad, sir.")
                try:
                    os.startfile("notepad.exe")
                except Exception as e:
                    speak("Sorry sir, I am unable to open Notepad.")

            elif "open calculator" in query:
                speak("Opening Calculator, sir.")
                try:
                    os.startfile("calc.exe")
                except Exception as e:
                    speak("Sorry sir, I am unable to open Calculator.")
            
            elif "open google" in query:
                speak("Opening Google, sir.")
                webbrowser.open("https://www.google.com")
            
            elif "open youtube" in query:
                speak("Opening YouTube, sir.")
                webbrowser.open("https://www.youtube.com")

            elif "open chrome" in query:
                speak("Opening Google Chrome, sir.")
                try:
                    webbrowser.open("https://www.google.com")
                except Exception as e:
                    speak("Sorry sir, I am unable to open Chrome.")

            elif query in ["goodbye vani", "goodbye", "exit", "bye", "thanks", "thank you", "stop", "ok bye"]:
                speak("Goodbye sir, have a great day!")
                break  

            # Fallback ab Wikipedia ke paas jaayega
            else:
                # User ke sawaal ko saaf karein (jaise 'who is', 'what is')
                if "who is" in query:
                    query = query.replace("who is", "")
                elif "what is" in query:
                    query = query.replace("what is", "")
                elif "tell me about" in query:
                    query = query.replace("tell me about", "")
                
                response_text = ask_wikipedia(query)
                speak(response_text)

        except KeyboardInterrupt:
            print("\nShutting down by user request (Ctrl+C).")
            speak("Goodbye sir.Have a Nice day")
            break