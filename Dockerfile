FROM python:3.9-slim


WORKDIR app

COPY . .

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-pip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
RUN pip install django
# Expose port 8000
EXPOSE 8000
# Start the Django development server
CMD ["python","manage.py","runserver","0.0.0.0:8000"]
