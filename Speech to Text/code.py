import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Reading Microphone as source
# Listening to the speech and storing it in the audio_text variable
with sr.Microphone() as source:
    print("Talk")
    
    # Adjust the timeout (in seconds) according to your preference
    audio_text = r.listen(source, timeout=5)
    
    print("Time over, thanks")

# Recognize the speech
try:
    # Using Google Speech Recognition
    print("Text: " + r.recognize_google(audio_text))
except sr.UnknownValueError:
    print("Sorry, I did not get that")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")
