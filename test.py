
import speech_recognition as s


def takeQuery():
    sr = s.Recognizer()
    sr.pause_threshold = 2
    print("speak")
    with s.Microphone() as m:
        try:
            audio = sr.listen(m)
            query = sr.recognize_google(audio, language='eng-in')
            return query

        except Exception as e:
            print("exception in this",e)
            print("not recognized")
query=takeQuery()
print(query)