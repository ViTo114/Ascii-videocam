import cv2 as cv

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

    # La stringa indica il nome della finestra che verrà creata
    cv.imshow("camera", frame)

    # Con questa istruzioni specifichiamo che il programma si deve arrestare per un 1 millisecondo
    # per controllare se ho premuto il tasto q
    if cv.waitKey(1) == ord('q'):
        break

camera.release()
cv.destroyAllWindows()