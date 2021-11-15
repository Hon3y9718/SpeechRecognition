from vosk import Model, KaldiRecognizer
from pyaudio import PyAudio, paInt16
import sys, pyttsx3, time

class SpeechReconition():
    def __init__(self) -> None:
        #Speech Recognition Model by Vosk*
        model = Model('vosk-model-en-in-0.4')
        self.recognizer = KaldiRecognizer(model, 16000)

        #Capture Microphone
        #Starting Stream of Microphone Capture
        cap = PyAudio()
        self.stream = cap.open(format=paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
        self.stream.start_stream()

        #TTS Engine
        self.engine = pyttsx3.init()
        self.engine = pyttsx3.init()
        prop = self.engine.getProperty('voices')
        self.engine.setProperty('voice', prop[1].id)
        self.engine.setProperty("rate", 178)

    '''
        recognize uses Vosk to recognize voice in realtime (Offline).
        It can listen to the Microphone and Detect/Recognize everything said.
    '''
    #STT using Mic
    def recognize(self):
        audio = self.stream.read(4196)
        if self.recognizer.AcceptWaveform(audio):
            result = self.recognizer.Result()
            result = result.replace("\n", "").replace("{", "").replace("}","").replace('"text"', "").replace(":", "").split('"')[1]
            if result != "" and result is not None:
                return result
            else:
                return "''"
        return "''"

    '''
        Use listen when you want only voice from your mic. 
        It will return to you the Audio which can be stored in .wav or .mp3 format
    '''
    def listen(self, chunkSize=4196):
        audio = self.stream.read(chunkSize)
        return audio    

    '''
        Speak will Speak English sentences in the Voice of Hazel which is the index:1 voice in This PC.
        To change the voice look the Constructor of Speech Recognition Class
    '''
    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

'''
####   Example of Usage   ####

obj = SpeechReconition() # Object creation of SpeechRecognition Class
while True:
    result = obj.recognize() # Starting Recognition of Voice from Microphone and Printing in the Terminal...
    print(result)   
    if 'bye' in result:
        obj.speak("Good Bye!...") # Says Good Bye... using speak Function
        time.sleep(2)
        sys.exit() #Exits

####   End of Usage   ####
'''