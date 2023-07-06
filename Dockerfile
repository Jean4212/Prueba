# Usa una imagen base de Linux ligero
FROM alpine:latest

# Copia los archivos de tu proyecto al contenedor
COPY . /app

# Establece el directorio de trabajo
WORKDIR /app

# Instala Python y otras dependencias necesarias
RUN apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --no-cache --upgrade pip setuptools && \
    pip3 install --no-cache -r requirements.txt

# Expone el puerto 80 para acceder a la aplicación
EXPOSE 80

# Comando para ejecutar el servidor de FastAPI
CMD ["python3", "app.py", "--host", "0.0.0.0", "--port", "80"]
