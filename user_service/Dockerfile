
FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code/user-service

RUN pip install --no-cache-dir --upgrade user_service==1.0.0

CMD ["fastapi", "run", "/code/user-service/src/main/python/api/main.py", "--port", "8770"]

#CMD ["fastapi", "run", "/usr/lib/python3/site-packages/user_service/main/python/api/main.py", "--port", "8770"]