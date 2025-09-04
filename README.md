# live-voice-translator

Real-time voice translation from spoken language to Turkish using speech recognition and Google Translate.

## Requirements

- **Python 3.8 or newer** (tested on Python 3.8 and 3.13.3).
- A working **microphone** or a system **loopback device** (e.g. Stereo Mix or Loopback) to capture audio from your computer.
- An **internet connection** for translation via Google Translate.

## Installation

1. **Clone the repository**:

    git clone https://github.com/furkanayid/live-voice-translator.git
    cd live-voice-translator

2. (**Optional**) **Create and activate a virtual environment** to isolate dependencies:

    python3 -m venv .venv
    # On Linux/macOS
    source .venv/bin/activate
    # On Windows
    .venv\Scripts\activate

3. **Install the required Python packages** using pip:

    pip install SpeechRecognition
pip install googletrans==4.0.0-rc1
    pip install pyaudio

    If you encounter errors installing **PyAudio**:

    - On **Linux**, install PortAudio development headers before installing PyAudio:

        sudo apt-get install portaudio19-dev
        pip install pyaudio

    - On **Windows**, if pip install pyaudio fails, download a matching wheel from the [PyAudio downloads](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) and install it:

        pip install <wheel-file>

    - On **macOS**, install PortAudio via Homebrew:

        brew install portaudio
        pip install pyaudio

## Usage

Run the script from the repository root:

    python voice_translator.py

A white window will open. Speak into your microphone (or play audio from your computer). The script will attempt to use a system loopback device (e.g. "Stereo Mix" or "Loopback") to capture audio directly from your speakers; if none is available it falls back to the default microphone. Recognized English speech will be translated into Turkish and displayed in the window in real time. Press Ctrl+C at any time to stop listening and exit the program.

## Notes

- This script uses Google’s unofficial translation service via the googletrans library. It may be subject to rate limits or reliability issues.
- Ensure your microphone or system loopback device is selected as the default input device on your system. You can adjust the ambient noise calibration in the code if needed.
- When using Python 3.13, install googletrans==4.0.0-rc1 (note the hyphen). Other pre-release versions like 4.0.0rc1 may cause import errors.
