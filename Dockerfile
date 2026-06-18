FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    git
    
RUN pip3 install pyYAML --break-system-packages

COPY portfolio.py /usr/bin/portfolio.py

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]
