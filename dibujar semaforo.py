import cv2

def dibujar_semaforo(frame, estado, nombre=""):
    """
    Dibuja un indicador visual en la pantalla según el estado.
    Estados: 0 = Buscando, 1 = Acceso/Verde, 2 = Retardo/Amarillo, 3 = Denegado/Rojo
    """
    # Configuración del círculo (esquina superior derecha)
    centro = (580, 50)
    radio = 20
    grosor = -1 # Relleno completo
    
    if estado == 1: # VERDE: Acceso concedido
        color = (0, 255, 0)
        mensaje = f"BIENVENIDO: {nombre}"
    elif estado == 2: # AMARILLO: Retardo
        color = (0, 255, 255)
        mensaje = "RETARDO DETECTADO"
    elif estado == 3: # ROJO: Denegado / Intruso
        color = (0, 0, 255)
        mensaje = "ALERTA: DESCONOCIDO"
    else: # GRIS: Buscando...
        color = (169, 169, 169)
        mensaje = "ESCANEANDO ROSTRO..."

    # Dibujar el círculo del semáforo
    cv2.circle(frame, centro, radio, color, grosor)
    
    # Dibujar el texto de estado
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, mensaje, (10, 50), font, 0.8, color, 2, cv2.LINE_AA)

# --- Ejemplo de integración en tu bucle principal de OpenCV ---
# cap = cv2.VideoCapture(0)
# while True:
#     ret, frame = cap.read()
#     # Aquí iría tu lógica de reconocimiento facial
#     # resultado_validacion = validar_rostro() 
#
#     dibujar_semaforo(frame, estado=1, nombre="Tu Nombre") # Ejemplo de acceso
#
#     cv2.imshow('Sistema de Asistencia FIMAZ', frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break