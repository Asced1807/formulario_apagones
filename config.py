import os

class Config:
    DB_NAME = os.getenv('DB_NAME', 'formulario_apagones')  # Nombre de la base de datos
    DB_USER = os.getenv('DB_USER', 'postgres')  # Usuario de PostgreSQL
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'elvin123')  # Contraseña de PostgreSQL
    DB_HOST = os.getenv('DB_HOST', 'db')  # Este será el nombre del servicio del contenedor de PostgreSQL
    DB_PORT = os.getenv('DB_PORT', '5432')  # Puerto de PostgreSQL
