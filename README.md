# Docker workshop

Currently there is a very minimal setup for creating docker images that can be 
used to create interactive python apps that process a text input and provide a
text output. 

Clone the directory and run this to start the app: 

```
docker build -t text-processor .
docker run -p 5000:5000 text-processor
```

Then you should be able to find the app on: http://localhost:5000/