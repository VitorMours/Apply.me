FROM python:3.12.13

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/root/.local/bin:$PATH"

WORKDIR /app

# Instala o uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Copia dependências
COPY requirements.txt .

# Instala as dependências globalmente
RUN uv pip install --no-cache --system -r requirements.txt

COPY . .

EXPOSE 8000

# Usamos o 'uv run' para garantir que o binário 'uvicorn' seja encontrado
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]