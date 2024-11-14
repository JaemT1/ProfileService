# Usa una imagen base oficial de Python
FROM python:3.12-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de requerimientos al contenedor
COPY requirements.txt .

# Crea un entorno virtual y actívalo
RUN python -m venv /app/venv

# Instala las dependencias en el entorno virtual
RUN /app/venv/bin/pip install --no-cache-dir -r requirements.txt

# Copia el contenido del proyecto al contenedor
COPY . .

# Configura las variables de entorno para Django y PostgreSQL
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=ProfileService.settings
ENV POSTGRES_DB=profiles_db
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=ROOT
ENV DB_HOST=db_profiles
ENV DB_PORT=5435
ENV PATH="/app/venv/bin:$PATH"


# Expone el puerto en el que correrá el servidor Django
EXPOSE 8000

# Ejecuta las migraciones y lanza el servidor de desarrollo
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
