FROM python:2.7-wheezy

# Install locust
RUN pip install pyzmq locustio faker

ADD scenario /root
ADD main.py /root

EXPOSE 5000

WORKDIR /root
ENTRYPOINT ["/root/main.py"]