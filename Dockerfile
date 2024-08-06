FROM python:3.12.0
WORKDIR /usr/app/
COPY . /usr/app/
EXPOSE 5000
RUN pip install -r requirements.txt
CMD ["python","app.py"]

