import cv2 as cv
import numpy as np
import os



# Funzione per associare un carattere ascii ad ogni livello di intensità
def intensita2Ascii (intensita):
    carattere = " +I%$@"

    indice = intensita // 43

    return carattere[indice]


# Funzione per trasformare il frame in una matrice numpy di caratteri
def frame2AsciiFrame (frame):
    dimensioni = frame.shape

    asciiFrame = np.empty(dimensioni, dtype='U1')

    for riga in range(dimensioni[0]):
        for colonna in range(dimensioni[1]):
            asciiFrame[riga, colonna] = intensita2Ascii(frame[riga, colonna])

    return asciiFrame


def printAsciiFrame(asciFrame):
    os.system("clear")

    immagine = ""

    dimensioni = asciFrame.shape

    for riga in range(dimensioni[0]):
        immagine = immagine + "\n"
        for colonna in range(dimensioni[1]):
            immagine = immagine + asciFrame[riga, colonna]

    print(immagine)




# il paramentro 0 rappresenta la camere di default del pc
camera = cv.VideoCapture(0)

if not camera.isOpened():
    print("Impossibile accedere alla webcam del pc")
    exit()

# L'oggetto VideoCapture permette di ottenere un frame alla volta.
# Quindi usiamo un ciclo while per ottenere più frame
while True:
    ret, frame = camera.read()

    # ret rappresenta un valore booleno che assume valore positivo quando
    # la funzione read() acquisice correttamente il frame
    if not ret:
        print("Il programma non riece a ricevere i frame dalla camnera")
        break

    frame = cv.resize(frame, (300, 100))

    # Questa istruzioni applica il filtro bianco e nero al frame catturato
    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    asciiFrame = frame2AsciiFrame(frame)

    printAsciiFrame(asciiFrame)


camera.release()