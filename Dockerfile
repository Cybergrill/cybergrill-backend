FROM python:3.9

WORKDIR /app

# Instalar o Poetry
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/etc/poetry python3 -
ENV PATH="$HOME/.poetry/bin:$PATH"

# Copiar e instalar as dependências do projeto com o Poetry
COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

# Copiar o resto do projeto
COPY . .

# Executar o servidor Django
CMD ["python", "manage.py", "runserver"]