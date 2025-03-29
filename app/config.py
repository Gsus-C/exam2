class Config:
    # Conexión a RDS usando las credenciales proporcionadas
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://jesus:jesus123@database-2.cn4gs86ao6m2.us-east-2.rds.amazonaws.com/users"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True  # Habilitar el modo de depuración para desarrollo