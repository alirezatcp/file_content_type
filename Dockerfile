FROM python:3.9-alpine
EXPOSE 8000
WORKDIR /app
RUN python -m venv venv && source venv/bin/activate
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python","manage.py", "runserver", "0.0.0.0:8000"]
