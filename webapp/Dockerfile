FROM python:3.11
RUN apt-get update -y
RUN apt-get upgrade -y
 

# System deps:
RUN pip install poetry==1.2.2

WORKDIR /app
COPY ./poetry.lock ./pyproject.toml ./
COPY ./app ./app
COPY ./README.md ./README.md
RUN poetry config virtualenvs.create false && poetry install
RUN poetry shell

  

CMD [ "uvicorn", "main:app", "--reload"]