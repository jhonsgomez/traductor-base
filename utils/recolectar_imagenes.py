import os
import cv2

DATA_DIR = "./dataset/imagenes"
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

number_of_classes = 6
dataset_size = 200

mensaje = '!Listo! - Presiona "Q" para continuar'
posicion = (10, 25)
fuente = cv2.FONT_HERSHEY_SIMPLEX
tamaño_fuente = 0.6
color_texto = (0, 0, 0)
grosor = 1
linea = cv2.LINE_AA

cap = cv2.VideoCapture(0)
for j in range(number_of_classes):
    if not os.path.exists(os.path.join(DATA_DIR, str(j))):
        os.makedirs(os.path.join(DATA_DIR, str(j)))

    print("Recopilando la seña: {}".format(j + 1))

    done = False
    while True:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        cv2.putText(
            frame, mensaje, posicion, fuente, tamaño_fuente, color_texto, grosor, linea
        )
        cv2.imshow("Traductor | Recolectando imagenes", frame)
        if cv2.waitKey(25) == ord("q"):
            break

    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        cv2.imshow("Traductor | Recolectando imagenes", frame)
        cv2.waitKey(25)
        cv2.imwrite(os.path.join(DATA_DIR, str(j), "{}.jpg".format(counter)), frame)

        counter += 1

cap.release()
cv2.destroyAllWindows()
