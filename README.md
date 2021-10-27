# 1. Setup development environment
## 1.1. Virtual Environment
- `virtualenv` is a tool to create isolated Python environments.
    - `venv` folders
- Need to **activate** before.

## 1.2. Install library
To install any library and use it, we will use the command:
- `pip install lib_name`

## 1.3. Understanding file `requirements.txt`
- Includes libraries to be used in our project.
- We will use the following libraries
    - `thefuzz`: Compare the similarity of 2 texts
    - `SpeechRecognition`: Convert **Speech** to **Text**
    - `pyttsx3`: Convert **Text** to **Speech**
- To install all libraries in `requirements.txt`, we will use the command:
    - `pip install -r requirements.txt`
    
## 1.4. Running `.py` file
- Need activate venv before
- Run command: `python filename.py`


# 2. Comparing Similarity of 2 Texts
- Compare character similarity **not semantic**
- Import library
    - `from thefuzz import fuzz`
- Compare: `ratio = fuzz.ratio("this is a test", "this is a test!)`

# 3. Speech to Text
- We will use `SpeechRecognition` to convert **speech => text**
- Import library
    - `import speech_recognition as sr`
- Open Microphone
- Filter Noise
- Listen
    - `timeout`
    - `phrase_time_limit`
- Convert speech to text
```
import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    recognizer.adjust_for_ambient_noise(source)
    print("Listening")
    audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio, language='en')
        print(text)
    except sr.UnknownValueError:
        print("Don't know!!!")
    except sr.RequestError:
        print("Network Error!!!")
```

# 4. Text to speech
- We will use `pyttsx3` to convert **text => speech**
- Import library
    - `import pyttsx3`
- Initialize engine
- Convert text to speech
```
import pyttsx3

engine = pyttsx3.init()
engine.say("hello, how are you?")
engine.runAndWait()
```


[comment]: <> (## 1.5. Preparing Questions and Answers)

[comment]: <> (- Prepare questions and corresponding answers for each question.)

[comment]: <> (- Questions in `Questions.txt` and Answers in `Answers.txt`)

[comment]: <> (- **Note:** Each question and each answer is only on one line)
