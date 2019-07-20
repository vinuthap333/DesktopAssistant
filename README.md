# DesktopAssistant
DesktopAssistant  is an interactive assistant ,which takes user's voice command as input and performs activities such las playing music, sending email and more
It requries follwing python modules:
   pyttsx3,
   datetime,
   speech_recognition,
   wikipedia,
   webbrowser,
   os,
   smtplib,
   requests,
   random

random, requests, webbrowser, smtplib, os, datetime are built-in modules ,where as pyttsx3, speech_recognition and wikipedia needs to be installed externally  

# pyttsx3

pyttsx3 is a text-to-speech conversion library in Python

# speech_recoginition

Speech recognition is the process of converting spoken words to text. Python supports many speech recognition engines and APIs, including Google Speech Engine, Google Cloud Speech API, Microsoft Bing Voice Recognition and IBM Speech to Text.

# wikipedia

Wikipedia is a Python library that makes it easy to access and parse data from Wikipedia.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install pyttsx3
pip install speech_recognition
pip install wikipedia
```
## Usage

```python
import pyttsx3
import speech_recognition
import wikipedia


pyttsx3.init('sapi5') # returns pyttsx3.Engine 
speech_recognition.listen(source) 
wikipedia.summary(query, sentences=2) 
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
  
  
  
  
 
 
