FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY ./requirements/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app /app

EXPOSE 80

WORKDIR /app

CMD ["uvicorn", "app.api.main:app", "--host", "0.0.0.0", "--port", "80"]
