# Simple Web Server written in 'Python 3.x'
Displays 
 * Sample - Hello World message
 * Hostname
 * $PID

## Clone the repository

```
git clone https://github.com/ankit-shrivastava/python-hello-world.git
cd python-hello-world
```

## To Run:

```
python hello-world.py
```

## To Test:

```
curl http://localhost:80
*** Python - Hello World ! ***
Hostname is : <your-hostname>
Process ID  : <application-process-id>
```

## Docker

Can be used to create a docker image and run within a container

### To Build
```
docker build -t ankit-shrivastava/python-hello-world:latest .
```

### To Run
```
docker run -d -p 4779:80 ankit-shrivastava/python-hello-world:latest
```

### To Test under docker sever
```
curl http://localhost:4779
```
Result is
```
*** Python - Hello World ! ***
Hostname is : <docker-container-id>
Process ID  : 1%
```


### To Test from remote server
```
curl http://$(docker-machine ip default):4779
```
Result is
```
*** Python - Hello World ! ***
Hostname is : <docker-container-id>
Process ID  : 1%
```