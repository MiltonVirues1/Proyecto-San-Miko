import speech_recognition as sr
import webbrowser
import time
import pyttsx3
import os
import urllib.parse
import pyautogui

voz = pyttsx3.init() #Inicio del conversor de texto a voz del asistente
voz.setProperty('rate',150)
#Funcion para que el asistente entone palabras de texto a voz
def hablar(texto):
    print("San Miko: ",texto)
    voz.say(texto)
    voz.runAndWait()

#Funcion para escuchar el microfono del usuario(yo)
def escuchar():
    r=sr.Recognizer() #Inicia el driver de reconocimiento de voz
    with sr.Microphone() as source: # with utilizado para que una vez que el usuario dio la orden, esta funcion se libere sola
        print('Escuchando...')
        audio = r.listen(source)

    try: 
        comando = r.recognize_google(audio,language='es-AR') # variable para reconocer el idioma y acento del usuario
        print('Usuario: ', comando)
        return comando.lower() #Simplifica el reconocimiento de voz, pasando lo que el usuario diga a minusculas para evitar errores molestos
    except:
        print('Lo siento no entendi bien, podes volver a repetirlo porfavor?')
        return ""
while True:
    comando = escuchar()
    if 'miko' in comando or 'despierta' in comando: 
        hablar('Te escucho, milton')                      
        comando = escuchar()
    if "abrí música" in comando or "abrír música" in comando or 'música' in comando:
        hablar('Comprendido, iniciando Youtube Music')
        webbrowser.open("https://music.youtube.com/")
    elif 'chau' in comando or 'chao' in comando:
        hablar('Hasta luego, sensei')
        break
    elif 'pausa' in comando or 'pausar' in comando:
        hablar('Pausando...')
        pyautogui.press('playpause')
    elif 'volve' in comando or 'atrás' in comando:
        hablar('Retrocediendo al anterior...')
        pyautogui.press('prevtrack')
    elif 'próximo' in comando or 'siguiente' in comando:
        hablar('Pasando al proximo...')
        pyautogui.press('nexttrack')
    elif 'Google' in comando:
        hablar('Abriendo buscador de google...')
        webbrowser.open('https://www.google.com/?hl=es')
    elif 'Roblox' in comando or 'roblox' in comando:
        hablar('Entrando a roblox')
        os.startfile(r"C:\Users\NoxiePC\Desktop\Roblox Player.lnk")
    elif 'administrador de tareas' in comando:
        hablar('Comprendido, ejecutando administrador de tareas')
        os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\System Tools\Task Manager.lnk")
    elif 'navegar' in comando or 'buscar' in comando:
        hablar('Que deseas buscar?')
        comando = escuchar()
        if comando:
            query=urllib.parse.quote_plus(comando)
            url=f"https://www.google.com/search?q={query}"
            hablar(f"Buscando {comando} en Google.")
            webbrowser.open(url)
        else:
         hablar('No entendi la busqueda')
    elif 'panel de control' in comando:
        hablar('Abriendo panel de control')
        os.startfile(r"C:\Users\NoxiePC\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\System Tools\Control Panel.lnk")
    elif 'cmd' in comando:
        hablar('Abriendo Simbolo del sistema')
        os.startfile(r"C:\Users\NoxiePC\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\System Tools\Command Prompt.lnk")
    elif 'este equipo' in comando:
        hablar('Abriendo Este equipo')
        os.startfile(r"C:\Users\NoxiePC\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\System Tools\computer.lnk")
    elif comando.strip() != "":
     print("Comando no reconocido:", comando)
    
    

    
