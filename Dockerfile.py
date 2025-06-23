FROM debian:stable-slim
COPY main.py main.py
COPY books/ books/

# Updating the system
RUN apt update
RUN apt upgrade -y

# Installing python3
RUN apt install python3 -y

# Installing python3-pip
RUN apt install python3-pip -y


CMD ["python3", "main.py"]
