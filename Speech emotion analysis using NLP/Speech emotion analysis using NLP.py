import speech_recognition as sr
from textblob import TextBlob

# Initialize recognizer
recognizer = sr.Recognizer()

# Record audio from the microphone
with sr.Microphone() as source:
    print("Please speak something...")
    audio = recognizer.listen(source)

try:
    # Recognize speech using Google Web Speech API
    text = recognizer.recognize_google(audio)
    print("You said: ", text)

    # Perform sentiment analysis using TextBlob
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity

    if sentiment_score > 0.2:
        emotion = "Happy"
    elif sentiment_score < -0.2:
        emotion = "Sad"
    else:
        emotion = "Neutral"

    print("Emotion detected:", emotion)

except sr.UnknownValueError:
    print("Sorry, could not understand audio.")
except sr.RequestError:
    print("Sorry, could not request results.")
