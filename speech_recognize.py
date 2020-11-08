import speech_recognition as sr

def main():
  mic = sr.Recognizer()
  with sr.Microphone() as source:
    mic.adjust_for_ambient_noise(source)
    print(f'Fale algo: ')
    audio = mic.listen(source)
  
  try:
    text = mic.recognize_google(audio, language = "pt-BR")
    print(f'Você disse: {text}')
  except sr.UnkownValueError:
    print(f'Não entendi')

  return text

if __name__== "__main__":
  main()