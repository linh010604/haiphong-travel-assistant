# Import library
import pyttsx3
# Initialize engine
engine = pyttsx3.init()

# Convert text to speech
engine.say("Hello, my name is Tuan")
# runAndWait
engine.runAndWait()
