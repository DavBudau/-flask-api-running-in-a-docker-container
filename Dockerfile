FROM python:3.9-alpine
COPY . /app
WORKDIR /app/api
RUN pip install -r ./requirements.txt
RUN adduser -D myuser
USER myuser
ENTRYPOINT ["python"]
CMD ["main.py"]