import cv2

# Configuración de umbrales
UMBRAL_CONFIANZA = 0.8  # 80% de seguridad para ponerse en verde
frames_positivos = 0
REQUISITO_ESTABILIDAD = 10 # Cuántos frames seguidos debe verte para confirmar

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret: break

    # Simulación de "confianza" de la red neuronal (aquí iría tu modelo)
    # Por ahora usaremos un valor de ejemplo:
    confianza_actual = 0.85 

    # Lógica de Umbrales
    if confianza_actual >= UMBRAL_CONFIANZA:
        frames_positivos += 1
    else:
        frames_positivos = 0

    # Dibujar Semáforo basado en estabilidad
    if frames_positivos >= REQUISITO_ESTABILIDAD:
        color_semaforo = (0, 255, 0) # Verde - Acceso Confirmado
        texto = "ESTADO: ACCESO"
    elif frames_positivos > 0:
        color_semaforo = (0, 255, 255) # Amarillo - Procesando...
        texto = "ESTADO: VERIFICANDO"
    else:
        color_semaforo = (0, 0, 255) # Rojo - No detectado
        texto = "ESTADO: BUSCANDO"

    # Interfaz Visual
    cv2.circle(frame, (50, 50), 20, color_semaforo, -1)
    cv2.putText(frame, texto, (80, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color_semaforo, 2)
    
    cv2.imshow('Propuesta Umbrales - Tesis FIMAZ', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()