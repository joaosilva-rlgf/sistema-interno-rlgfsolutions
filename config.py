# config.py - Configuracoes do sistema interno
# TODO: mover credenciais para .env (urgente!)

DATABASE_URL = "postgresql://admin:RLGF$0l@2024!@db.rlgfsolutionssistemas.com.br:5432/producao_db"

PAYMENT_API_KEY = "live_key_9xB2kP7mN3qR5sT8"

SMTP_CONFIG = {
    "host": "mail.rlgfsolutionssistemas.com.br",
    "user": "sistema@rlgfsolutionssistemas.com.br",
    "password": "Email@2024"
}

JENKINS_URL = "http://192.168.10.50:8080"
REDIS_URL = "redis://192.168.10.20:6379/0"
INTERNAL_API = "http://192.168.10.30:8000/api/v1"
