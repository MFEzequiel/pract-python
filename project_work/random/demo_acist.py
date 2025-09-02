import speech_recognition as sr
import pyttsx3
import win32com.client
import os

def iniciar_escritura():
    try:
        word = os.system("star WorPad")
        word.Visible = True
        doc = word.Documents.Add()
        return doc
    except Exception as e:
        print(f"No se pudo iniciar Word. Error: {e}")
        return None

def finalizar_escritura(doc):
    try:
        doc.SaveAs(r"F:\ruta\nuevo.docx")
        doc.Close()
    except Exception as e:
        print(f"No se pudo guardar el documento. Error: {e}")

def dictar_en_word():
    recognizer = sr.Recognizer()
    engine = pyttsx3.init()

    with sr.Microphone() as source:
        print("Escuchando... Di 'comienza a escribir' para iniciar y 'detén escritura' para terminar.")
        audio = recognizer.listen(source)

    try:
        texto = recognizer.recognize_google(audio, language="es-ES").lower()

        if "comienza a escribir" in texto:
            doc = iniciar_escritura()
            if doc is not None:
                engine.say("Comienza a dictar. Di 'detén escritura' cuando hayas terminado.")
                engine.runAndWait()

                while True:
                    audio = recognizer.listen(source)
                    texto = recognizer.recognize_google(audio, language="es-ES").lower()

                    if "detén escritura" in texto:
                        finalizar_escritura(doc)
                        engine.say("Escritura finalizada. El documento ha sido guardado.")
                        engine.runAndWait()
                        break
                    else:
                        doc.Content.InsertAfter(texto)
        else:
            engine.say("No entendí el comando.")
            engine.runAndWait()

    except sr.UnknownValueError:
        engine.say("No se pudo entender el audio.")
        engine.runAndWait()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    dictar_en_word()