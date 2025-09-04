import speech_recognition as sr
from googletrans import Translator
import tkinter as tk
import pyaudio

def get_loopback_device_index():
    """Return device index for system audio loopback if available (e.g. Stereo Mix or Loopback)."""
    p = pyaudio.PyAudio()
    loop_idx = None
    for i in range(p.get_device_count()):
        dev = p.get_device_info_by_index(i)
        name = dev.get('name', '').lower()
        if 'stereo mix' in name or 'loopback' in name:
            loop_idx = i
            break
    p.terminate()
    return loop_idx


import threading


def listen_and_translate(update_callback, src_lang="en", dest_lang="tr"):
    """Listen to microphone input, translate it, and call update_callback with the result."""
    recognizer = sr.Recognizer()
    translator = Translator()
    device_index = get_loopback_device_index()
    if device_index is not None:
        mic = sr.Microphone(device_index=device_index)
    else:
        mic = sr.Microphone()


    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        while True:
            try:
                # Listen for speech from the microphone
                audio = recognizer.listen(source)
                # Recognize speech using the specified language
                text = recognizer.recognize_google(audio, language=src_lang)
                print(f"Recognized: {text}")

                # Translate recognized text to the destination language
                translation_result = translator.translate(text, src=src_lang, dest=dest_lang)
                translated_text = translation_result.text
                print(f"Translated: {translated_text}")

                # Update the GUI with the translated text
                update_callback(translated_text)
            except Exception as e:
                # Handle errors (e.g., network issues or unrecognized speech)
                print("Error:", e)


def main():
    # Create the main application window
    root = tk.Tk()
    root.title("Live Voice Translator")
    root.configure(bg="white")
    root.geometry("800x200")

    # Label to display the translated text
    label = tk.Label(root, text="", font=("Arial", 16), bg="white", wraplength=780, justify="left")
    label.pack(padx=10, pady=10)

    # Define a function to update the label text
    def update_label(text):
        label.config(text=text)

    # Start the listening and translation in a background thread
    thread = threading.Thread(target=listen_and_translate, args=(update_label,), daemon=True)
    thread.start()

    # Start the Tkinter event loop
    root.mainloop()


if __name__ == "__main__":
    main()
