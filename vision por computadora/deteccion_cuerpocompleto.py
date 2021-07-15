print("Hola")

import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic

with mp_holistic.Holistic(
    static_image_mode=True, #True porque es una imagen estatica
    model_complexity=1) as holistic: #(0 al 2) el numero mas grande es mas preciso el modelo

    #cargamos la imagen
    image = cv2.imread("./posturewomen.jpg")

    #la procesamos en colores
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = holistic.process(image_rgb)


    #detectamos y marcamos el rostro
    mp_drawing.draw_landmarks(image, results.face_landmarks, mp_holistic.FACE_CONNECTIONS,
    mp_drawing.DrawingSpec(color=(0,255,255), thickness=1, circle_radius=1),
    mp_drawing.DrawingSpec(color=(0,128,255), thickness=2))

    #detectamos y marcamos la mano izquierda
    mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
    mp_drawing.DrawingSpec(color=(255,255,0), thickness=1, circle_radius=1),
    mp_drawing.DrawingSpec(color=(0,128,255), thickness=2))

    #detectamos y marcamos la mano derecha
    mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
    mp_drawing.DrawingSpec(color=(0,255,0), thickness=1, circle_radius=1),
    mp_drawing.DrawingSpec(color=(57,143,0), thickness=2))

    #detectamos la estructura del cuerpo
    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS,
    mp_drawing.DrawingSpec(color=(128,0,255), thickness=1, circle_radius=1),
    mp_drawing.DrawingSpec(color=(255,255,255), thickness=2))

    #mostramos la foto
    cv2.imshow("Image", image)

    #ploteamos los puntos de la postura del cuerpo y hacemos las conexiones
    mp_drawing.plot_landmarks(
        results.pose_world_landmarks, mp_holistic.POSE_CONNECTIONS
    )

    #detenemos la aplicacion
    cv2.waitKey(0)

#-------------------------------------
#SEGUNDA PARTE DEMOSTRACION CON VIDEO
#-------------------------------------

#cargamos el video
cap = cv2.VideoCapture("./dancing_woman.mp4")
#cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) #por streaming, se requiere una webcam instalada


with mp_holistic.Holistic(
    static_image_mode=False, #False proque es video
    model_complexity=1) as holistic: #(0 al 2, entre mayor mas precision pero mas lento procesamiento)

    while True:
        ret, frame = cap.read()
        if ret==False:
            break

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = holistic.process(frame_rgb)

           #detectamos y marcamos el rostro
        mp_drawing.draw_landmarks(frame, results.face_landmarks, mp_holistic.FACE_CONNECTIONS,
        mp_drawing.DrawingSpec(color=(0,255,255), thickness=1, circle_radius=1),
        mp_drawing.DrawingSpec(color=(0,128,255), thickness=2))

        #detectamos y marcamos la mano izquierda
        mp_drawing.draw_landmarks(frame, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
        mp_drawing.DrawingSpec(color=(255,255,0), thickness=1, circle_radius=1),
        mp_drawing.DrawingSpec(color=(0,128,255), thickness=2))

        #detectamos y marcamos la mano derecha
        mp_drawing.draw_landmarks(frame, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
        mp_drawing.DrawingSpec(color=(0,255,0), thickness=1, circle_radius=1),
        mp_drawing.DrawingSpec(color=(57,143,0), thickness=2))

        #detectamos la estructura del cuerpo
        mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS,
        mp_drawing.DrawingSpec(color=(128,0,255), thickness=1, circle_radius=1),
        mp_drawing.DrawingSpec(color=(255,255,255), thickness=2))

        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) & 0xFF==27:
            break


cv2.destroyAllWindows()
