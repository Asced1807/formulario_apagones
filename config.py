import os

class Config:
    # Usamos la variable de entorno DATABASE_URL si está disponible
    # Si no, utilizamos los valores predeterminados proporcionados por Railway
    DATABASE_URL = os.getenv(
        'DATABASE_URL', 
        'postgresql://postgres:DDGbJwlwTxIfkogqoLakllnwAkmKyMgp@postgres-olkg.railway.internal:5432/ferrocarril?sslmode=require'
    )

    # Si prefieres definir las configuraciones por separado (esto no es necesario si usas DATABASE_URL):
    DB_NAME = os.getenv('DB_NAME', 'ferrocarril')  # Nombre de la base de datos en Railway
    DB_USER = os.getenv('DB_USER', 'postgres')  # Usuario de PostgreSQL
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'DDGbJwlwTxIfkogqoLakllnwAkmKyMgp')  # Contraseña de PostgreSQL
    DB_HOST = os.getenv('DB_HOST', 'postgres-olkg.railway.internal')  # Host proporcionado por Railway
    DB_PORT = os.getenv('DB_PORT', '5432')  # Puerto de PostgreSQL (predeterminado)

