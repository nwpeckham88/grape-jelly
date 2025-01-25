FROM alpine:3.7
RUN apk add --no-cache python3 py3-pip ffmpeg python3-dev
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . /app
WORKDIR /app
CMD ["python3", "src/main.py"]