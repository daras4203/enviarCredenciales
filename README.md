# 📧 ENVIARCREDENCIALES

Automatización en Python para el envío masivo de correos electrónicos con credenciales a usuarios listados en un archivo Excel.

---

## 📁 Estructura del proyecto

```
ENVIARCREDENCIALES/
├── data/
│   └── usuarioCorreo.xlsx     # Archivo Excel con los usuarios y correos destino
├── config.py                  # Configuración general (credenciales, parámetros SMTP)
├── correo.py                  # Módulo para el envío de correos electrónicos
├── leerExcel.py               # Módulo para la lectura del archivo Excel
└── main.py                    # Punto de entrada principal del programa
```

---

## 📋 Descripción de archivos

### `data/usuarioCorreo.xlsx`
Archivo Excel que contiene la lista de usuarios. Debe tener las siguientes columnas:

| Nombre | email |
|--------|-------|
| Juan Pérez | juan@empresa.com |
| María López | maria@empresa.com |

### `config.py`
Contiene los parámetros de configuración del proyecto:
- Credenciales del correo remitente
- Servidor SMTP y puerto
- Asunto del correo
- Ruta del archivo Excel

### `correo.py`
Módulo encargado de:
- Conectarse al servidor SMTP
- Construir el mensaje de correo
- Enviar el correo a cada destinatario

### `leerExcel.py`
Módulo encargado de:
- Leer el archivo `usuarioCorreo.xlsx`
- Retornar la lista de usuarios y correos

### `main.py`
Punto de entrada del programa. Orquesta el flujo:
1. Lee el Excel con `leerExcel.py`
2. Itera por cada usuario
3. Envía el correo con `correo.py`

---

## ⚙️ Requisitos

- Python 3.8+
- Librerías necesarias:

```bash
pip install openpyxl
```

---

## 🚀 Ejecución

```bash
python main.py
```

---

## 🔐 Configuración previa

Antes de ejecutar, edita `config.py` con tus datos:

```python
REMITENTE = "tucorreo@empresa.com"
PASSWORD  = "tu_contraseña"
SMTP_HOST = "smtp.office365.com"
SMTP_PORT = 587
ASUNTO    = "Distribución de credenciales"
RUTA_EXCEL = "data/usuarioCorreo.xlsx"
```

---

## ⚠️ Consideraciones

- Asegúrate de que el archivo Excel tenga los encabezados `Nombre` y `email` correctamente escritos.
- No compartas el archivo `config.py` con credenciales en repositorios públicos.
- Se recomienda usar variables de entorno o un archivo `.env` para manejar credenciales sensibles.

---

## 👤 Autor

Proyecto interno — Dario Asprilla A.
