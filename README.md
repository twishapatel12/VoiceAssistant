# Voice Assistant Project

## Overview
This project is a Python-based voice assistant that uses speech recognition and text-to-speech technologies to perform various tasks based on voice commands. It can search Wikipedia, open websites, play music, tell the time, and launch applications.

## Features
- **Speech Synthesis**: Uses `pyttsx3` for converting text to speech.
- **Speech Recognition**: Employs `speech_recognition` for converting spoken language into text.
- **Task Automation**: Integrates with `wikipedia`, `webbrowser`, `os`, and `datetime` to execute commands.
- **Interactive Greeting**: Greets the user based on the time of day and responds to queries.

## Skills Used
- Python
- Speech Recognition
- Text-to-Speech
- Web Automation
- File Handling
- Date and Time Operations

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/voice-assistant-project.git
   ```
2. Navigate to the project directory:
   ```bash
   cd voice-assistant-project
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the main script to start the voice assistant:
   ```bash
   python voice_assistant.py
   ```

2. The assistant will greet you and wait for your commands. You can use commands like:
   - "Search Wikipedia for [topic]"
   - "Open YouTube"
   - "Open Google"
   - "Open Stack Overflow"
   - "Play music"
   - "What is the time?"
   - "Open code"
   - "Thank you"

## Example
```python
Listening....
Recognizing....
User said: open google

Listening....
Recognizing....
User said: play music
```

## Acknowledgements
- Python Software Foundation
- Libraries used: `pyttsx3`, `speech_recognition`, `wikipedia`, `webbrowser`, `os`, `datetime`, `random`

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
