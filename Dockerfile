FROM python:3.11.3-buster

WORKDIR /newsletter

COPY ./requirements.txt ./requirements.txt
COPY ./newsletter.py ./newsletter.py

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV SENDGRID_API_KEY=""

CMD ["python", "newsletter.py"]


