import speech_recognition as sr
import webbrowser
import pyttsx3
import os

# Inicializar motor de voz
voz = pyttsx3.init()
voz.setProperty('rate', 150)

def hablar(texto):
    print("San Miko:", texto)
    voz.say(texto)
    voz.runAndWait()

def escuchar():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        audio = r.listen(source)

    try:
        comando = r.recognize_google(audio, language='es-AR')
        print("Usuario:", comando)
        return comando.lower() #Simplifica el reconocimiento de voz, pasando lo que el usuario diga a minusculas para evitar errores molestos
    except:
        hablar("Perdón, no entendí.")
        return ""

# Comienzo
hablar("Hola Milton, soy San Miko. Te escucho.")

while True:
    comando = escuchar()

    if "abrí música" in comando or "abrir música" in comando:
        hablar("Abriendo YouTube Music en el navegador.")
        webbrowser.open("https://music.youtube.com/")

    elif "reproducí algo" in comando or "iniciar música" in comando:
        hablar("Entendido Milton, ya la reproduzco.")
        webbrowser.open("https://music.youtube.com/watch?v=APYazXm6lH0&si=-KvMwprC4zLQ7-vS")

    elif "chau" in comando or "chao" in comando or "cerrar" in comando:
        hablar("Hasta luego, Milton.")
        break

    elif comando != "":
        hablar("Ese comando aún no lo conozco.")

    # Volver a escuchar
    hablar("¿Te escucho para otra orden?")

