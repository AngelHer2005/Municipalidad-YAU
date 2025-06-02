# Municipalidad de Yau - Sistema de Trámites Priorizados

Sistema web para la gestión y priorización de trámites municipales, utilizando Machine Learning para asignar prioridades y facilitar la atención eficiente de solicitudes ciudadanas.

## 🚀 Características principales

- Registro y gestión de trámites municipales.
- Priorización automática de trámites usando modelos de Machine Learning.
- Interfaz moderna y responsiva con TailwindCSS.
- Visualización de trámites priorizados y detalles de cada solicitud.
- Gestión de ciudadanos y seguimiento de estados de trámite.

## 🛠️ Tecnologías utilizadas

- **Backend:** Django 5.x
- **Frontend:** Django Templates + TailwindCSS
- **Base de datos:** MySQL
- **Machine Learning:** Integración para predicción de prioridad y congestión (personalizable)
- **Python 3.10+**

## 📦 Instalación y configuración

1. **Clona el repositorio:**
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd municipalidad_yau/municipalidad_yau
   ```

2. **Crea y activa un entorno virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configura la base de datos MySQL:**
   - Crea una base de datos llamada `municipalidad_yau_db`.
   - Ajusta usuario y contraseña en `settings.py` si es necesario.

5. **Aplica migraciones:**
   ```bash
   python manage.py migrate
   ```

6. **Crea un superusuario (opcional, para admin):**
   ```bash
   python manage.py createsuperuser
   ```

7. **Ejecuta el servidor de desarrollo:**
   ```bash
   python manage.py runserver
   ```

8. **Accede a la aplicación:**
   - [http://localhost:8000/](http://localhost:8000/)

## 📁 Estructura del proyecto

```
municipalidad_yau/
│
├── municipalidad_yau/         # Configuración principal Django
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── tramites/                  # Aplicación de gestión de trámites
│   ├── models.py
│   ├── views.py
│   ├── templates/
│   └── ...
│
├── manage.py
└── README.md
```

## 🤖 Priorización con Machine Learning

El sistema está preparado para integrar modelos de ML que asignan una prioridad y predicen congestión para cada trámite. Puedes personalizar la lógica en la app `tramites` según tus necesidades.

## 📄 Licencia

Este proyecto es de uso académico y puede ser adaptado libremente para fines educativos.

---

**Desarrollado por:**  
Ángel Hernán Alberto Patricio Arroyo
Municipalidad de Yau

