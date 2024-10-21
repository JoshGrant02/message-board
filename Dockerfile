# Use an official Python runtime as an image
FROM python:3.9

EXPOSE 5000

WORKDIR /api

COPY requirements.txt /api
RUN pip install -r requirements.txt

# Run app.py when the container launches
COPY /api /api
CMD python app.py
