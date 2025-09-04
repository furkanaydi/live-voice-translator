import speech_recognition as sr
from googletrans import Translator


def main():
    recognizer = sr.Recognizer()
    translator = Translator()
    mic = sr.Microphone()
    print("Please speak. Press Ctrl+C to exit.")

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        while True:
            try:
                print("Listening...")
                audio = recognizer.listen(source)
                text = recognizer.recognize_google(audio, language='auto')
                print("Heard:", text)
                translated = translator.translate(text, dest='tr').text
                print("Translated to Turkish:", translated)
            except KeyboardInterrupt:
                print("Exiting...")
                break
            except Exception as e:
                print("Error:", e)


if __name__ == "__main__":
    main()
