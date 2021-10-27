"""
Put together
    - Define a list of questions and corresponding answers
    - Listen to the question and find the most suitable answer.
    If you can't find the answer, say "I don't know".
"""
import speech_recognition as sr
import pyttsx3
from thefuzz import fuzz


def read_file(filename):
    with open(filename, mode='r', encoding='utf8') as fp:
        contents = fp.read()
        contents = contents.lower()
        return contents.splitlines()


def find_answer(ques, list_ques, list_answers):
    best_idx = 0
    best_score = -1
    for idx, ques_in_list in enumerate(list_ques):
        score = fuzz.ratio(ques.lower(), ques_in_list)
        if score > best_score:
            best_idx = idx
            best_score = score
    if best_score < 50:
        return "I don't know!"
    else:
        return list_answers[best_idx]


def say(text):
    global engine
    engine.say(text)
    engine.runAndWait()


if __name__ == '__main__':
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    engine = pyttsx3.init()

    questions = read_file('data/question.txt')
    answers = read_file('data/answer.txt')

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        while True:
            say("What information that you want to know?")
            print("Listening")
            audio = recognizer.listen(source, timeout=8)
            try:
                question = recognizer.recognize_google(audio, language='en')
                print(question)
                answer = find_answer(question, questions, answers)
                say(answer)
                say("Do you want to continue? Please say YES or NO!")
                print("Listening")
                audio = recognizer.listen(source, timeout=8)
                question = recognizer.recognize_google(audio, language='en')
                if 'yes' not in question.lower():
                    say("Bye. Have a good time!")
                    break
            except sr.UnknownValueError:
                print("Don't know!!!")
            except sr.RequestError:
                print("Network Error!!!")
