
FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code/user-service

CMD ["fastapi", "run", "/code/user-service/src/main/python/api/main.py", "--port", "8770"]