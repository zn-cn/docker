# golang 测试 docker使用记录

docker-compose.yml 如下：

```
version: '3'

services:
    go_test:
        build: .
        volumes:
            - /etc/localtime:/etc/localtime:ro
        ports:
            - "1323:1323"
        environment:
            - TZ=Asia/Shanghai
        container_name: go_test_app
        entrypoint: [ "bin/main" ]
```

Dockerfile 如下：

```
FROM golang:1.10

WORKDIR /app
COPY . .

ENV GOPATH "/app"
RUN go build -o bin/main src/main.go && rm -rf src
EXPOSE 1323

ENTRYPOINT [ "bin/main" ]
```

测试流程：

+ 在当前目录下 `docker-compose up` 即可

+ 若需修改代码，修改之后请使用`docker-compose build`，之后再使用 `docker-compose up` 

  经个人测试使用 `docker-compose down`之后再使用 `docker-compose up`，不会删除镜像（不懂，并不像官方介绍的会删除镜像）

tips:

+ 若需进入容器，可使用 `docker-compose exec go_test bash` （go_test 为 docker-compose.yml 文件中的服务名）

  而不用使用 docker container ls，查到相应的容器名字之后，再使用docker exec -it [container id] bash进入

+ ENTRYPOINT和CMD的区别请移步官网，这里简要介绍，Dockerfile中的CMD会被docker-compose.yml中的command覆盖，之后作为ENTRYPOINT的参数，所以一般二者是配合使用，CMD主要是用来做弹性参数