# Flask Docker+MySql Entorno

Proyecto básico de **Flask** ejecutado dentro de un contenedor **Docker**, con soporte para dos entornos:  
- Desarrollo (debug activado)  
- Producción (debug desactivado)  

## Descripción

Este proyecto demuestra cómo configurar una aplicación Flask con Docker y manejar entornos mediante variables de entorno (`ENVIRONMENT`).  

## Estructura del proyecto

```
flask-entorno/
│
├── app.py
├── requirements.txt
└── Dockerfile
```

## Instalación

1. **Clonar el repositorio:**
   1. git clone https://github.com/tuusuario/flask-docker-MySql-Env.git
   2. cd flask-entorno
   
2. **Construcción de Imágen:**
   docker build -t flask_entorno .

4. **Modo Debug:**
   docker run -e ENVIRONMENT=development -p 5000:5000 flask_entorno

5. **Modo Producción:**
   docker run -e ENVIRONMENT=production -p 5000:5000 flask_entorno

6. **Conexión a la Base de Datos:**
   1. Crear una nueva conexión:
      Ports: 3306
      User: root
      Pass: root
7. **Ejecutar comandos en la Base de Datos:**
   1. SHOW DATABASES;
   2. USE testdb;
   3. CREATE TABLE demo (id INT PRIMARY KEY, nombre VARCHAR(50));
   4. INSERT INTO demo VALUES (1, 'Santiago');
   5. SELECT * FROM demo;
8. **Verificar los datos ingresados en la carpeta destino de datos:**
   1. cd /var/lib/mysql
   2. ls
9. **¡Listo!**


