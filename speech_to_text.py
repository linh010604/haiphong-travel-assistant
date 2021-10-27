# Import library
import speech_recognition as sr

# Open microphone
recognizer = sr.Recognizer()
microphone = sr.Microphone()
# Filter noise
with microphone as source:
    recognizer.adjust_for_ambient_noise(source)
    # Listen
    print("Listening.....")
    audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print('wait...')
        print(text)
    except:
        print("Error!")
# Convert Speech to Text
