import speech_recognition as sr
import os
from err import noalsaerr

def main():
  mic = sr.Recognizer()
  with noalsaerr.noalsaerr() as n, sr.Microphone() as source:
    mic.adjust_for_ambient_noise(source)
    print(f'Fale algo: ')
    audio = mic.listen(source)
  
  try:
    text = mic.recognize_google(audio, language = "pt-BR")
    print(f'Você disse: {text}')

    lowercase_letters = text.lower()

    if lowercase_letters == 'abrir spotify':
      print(os.system('spotify'))
  except sr.UnkownValueError:
    print(f'Não entendi')

  return text

if __name__== "__main__":
  main()