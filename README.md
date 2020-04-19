
# Sire

## [Github Action Hackathon Winner](https://githubhackathon.com/)

![dragon-ball-super-zeno](https://user-images.githubusercontent.com/23444642/75755654-0b375380-5d55-11ea-82f5-1f111f1191fb.jpg)

An inspirational quotes app using Flask

### Build application
Build the Docker image manually by cloning the Git repo.
```
$ git clone https://github.com/MuLx10/Sire.git
$ docker build -t Sire .
```

### Download precreated image
You can also just download the existing image from [DockerHub](https://hub.docker.com/r/lvthillo/python-flask-docker/).
```
docker pull Sire
```

### Run the container
Create a container from the image.
```
$ docker run --name my-container -d -p 8080:8080 Sire
```

Now visit http://localhost:8080
