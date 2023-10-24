# Usa una imagen base de Python
FROM python:3.9

# Establece el directorio de trabajo en el contenedor
WORKDIR /appdock

# Copia los archivos de tu proyecto al contenedor
COPY . /appdock

# Instala las dependencias de tu proyecto
RUN pip install -r requirements.txt

# Expone el puerto 8000, que es el puerto por defecto de Django
EXPOSE 8000

# Comando para ejecutar tu aplicación Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]