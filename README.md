# Docker workshop

Currently there is a very minimal setup for creating docker images that can be 
used to create interactive python apps that process a text input and provide a
text output. 

Clone the directory and run this to start the app: 

```
docker build -t loud-text .
docker run -d -p 127.0.0.1:5001:5000 loud-text
```

Then you should be able to find the app on: http://localhost:5001/
