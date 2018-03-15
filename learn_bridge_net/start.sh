docker network create learn_docker-net
docker-compose up
docker network connect learn_docker-net learn_docker_app
docker network connect learn_docker-net learn_docker_mongo