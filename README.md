# live-voice-translator
Real-time voice translation from spoken language to Turkish using speech recognition and Google Translate.
## Requirements

- **Python 3.8+** (tested on Python 3.8 or higher).
- A working **microphone** to capture audio from your computer.
- An **internet connection** is required for translation via Google Translate.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/furkanaydi/live-voice-translator.git
   cd live-voice-translator
   ```

2. (**Optional**) **Create and activate a virtual environment** to isolate dependencies:

   ```bash
   python3 -m venv .venv
   # On Linux/macOS
   source .venv/bin/activate
   # On Windows
   .venv\Scripts\activate
   ```

3. **Install the required Python packages** using `pip`:

   ```bash
   pip install SpeechRecognition googletrans==4.0.0rc1 PyAudio
   ```

   - On **Linux**, you may need to install PortAudio development headers before installing PyAudio:
     `sudo apt-get install portaudio19-dev` then `pip install pyaudio`.
   - On **Windows**, if `pip install pyaudio` fails, download the appropriate wheel from [PyAudio downloads](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) and install it using `pip install <wheel-file>`.
   - On **macOS**, you can install PortAudio via Homebrew: `brew install portaudio` and then run `pip install pyaudio`.

## Usage

Run the script from the repository root and speak into your microphone; the recognized speech and its translation to Turkish will be printed to the console:

```bash
python voice_translator.py
```

Press `Ctrl+C` at any time to stop listening and exit the program.

## Notes

- This script uses Google’s unofficial translation service via the `googletrans` library. It may be subject to rate limits or reliability issues. For production use, consider using an official translation API.
- Make sure your microphone is selected as the default input device on your system. You can adjust the ambient noise calibration in the code if needed.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
