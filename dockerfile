FROM python

EXPOSE 80
RUN mkdir -p /usr/src/app
COPY hello-world.py /usr/src/app/hello-world.py
ENTRYPOINT ["python", "/usr/src/app/hello-world.py"]
