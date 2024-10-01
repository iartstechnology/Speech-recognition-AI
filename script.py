import speech_recognition as sr
import os

# Função para ouvir e reconhecer a fala
def ouvir_microfone():
    # Habilita o microfone do usuário
    microfone = sr.Recognizer()

    # Usando o microfone
    with sr.Microphone() as source:
        # Chama um algoritmo de redução de ruídos no som
        microfone.adjust_for_ambient_noise(source)

        # Frase para o usuário dizer algo
        print("Diga alguma coisa: ")

        # Armazena o que foi dito numa variável
        audio = microfone.listen(source)

        try:
            # Passa a variável para o algoritmo reconhecedor de padrões
            frase = microfone.recognize_google(audio, language='pt-BR')

            # Se o usuário disser "Google", abre o navegador Google Chrome
            if "Google" in frase or "navegador Google" in frase:
                os.system("start chrome")  # Abre o Google Chrome

            elif "Excel" in frase:
                os.system("start Excel.exe")

            # Retorna a frase pronunciada
            print("Você disse: " + frase)

        # Se não reconheceu o padrão de fala, exibe a mensagem
        except sr.UnknownValueError:
            print("Não entendi")

    return frase

ouvir_microfone()
