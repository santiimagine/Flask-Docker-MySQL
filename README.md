# Flask Docker Entorno

Proyecto básico de **Flask** ejecutado dentro de un contenedor **Docker**, con soporte para dos entornos:  
- Desarrollo (debug activado)  
- Producción (debug desactivado)  

## Descripción

Este proyecto demuestra cómo configurar una aplicación Flask con Docker y manejar entornos mediante variables de entorno (`ENVIRONMENT`).  

## Estructura del proyecto

flask-entorno/
│
├── app.py
├── requirements.txt
└── Dockerfile



## Instalación

1. **Clonar el repositorio:**
   git clone https://github.com/tuusuario/flask-docker-entornos.git
   cd flask-docker-entornos
   
2. **Construcción de Imágen:**
docker build -t flask_entorno .

4. **Modo Debug:**
   docker run -e ENVIRONMENT=development -p 5000:5000 flask_entorno

5. **Modo Producción:**
  docker run -e ENVIRONMENT=production -p 5000:5000 flask_entorno

