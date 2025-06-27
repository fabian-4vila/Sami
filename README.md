# 🧠 Sami - Asistente Personal por Voz

**Sami** es una IA local y privada que reconoce tu voz, identifica quién eres, entiende tus órdenes y ejecuta acciones, todo sin depender de la nube.

Inspirado en el quechua, _Sami_ significa "energía sagrada" o "esencia positiva".

## 🚀 ¿Qué puede hacer?

- Activación por hotword: “Sami”
- Reconocer quién habla (tú u otra persona)
- Entender órdenes como “guarda una nota” o “apaga la luz”
- Ejecutar acciones
- Registrar historial y notas por usuario

## 🔧 Estructura del Proyecto
```
sami/
├── .dockerignore              # Ignora archivos al construir el contenedor
├── .gitignore                 # Evita subir archivos sensibles o innecesarios
├── Dockerfile                 # Define la imagen de Docker para Sami
├── docker-compose.yml         # Orquesta los servicios (por ahora solo Sami)
├── README.md                  # Documentación del proyecto
├── requirements.txt           # Dependencias de Python
├── run.sh                     # Script auxiliar para ejecutar el asistente
├── main.py                    # Punto de entrada de Sami
├── audio_input.py             # Captura y transcribe audio del micrófono
├── hotword_detector.py        # Detecta la palabra clave "Sami"
│
├── data/                      # Datos de entrenamiento
│   └── entrenamiento/
│       └── .gitkeep
│
├── memory/                    # Memoria del asistente (historial, usuarios, notas)
│   ├── historial.json
│   ├── usuarios.json
│   └── notas/
│       └── .gitkeep
│
├── models/                    # Modelos de ML entrenados
│   └── .gitkeep
```