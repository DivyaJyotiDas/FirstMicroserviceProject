
FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code/user_service
RUN export PYTHONPATH="/code/user_service"


#RUN pip install --no-cache-dir --upgrade users==1.0.0

CMD ["fastapi", "run", "/code/user_service/users/router/main.py", "--port", "8770"]

#CMD ["fastapi", "run", "/usr/lib/python3/site-packages/users/main/python/api/main.py", "--port", "8770"]