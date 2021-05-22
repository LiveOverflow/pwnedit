.PHONY : all stop build run attach root
all : stop build run

stop:
	-docker stop sudo3
	sleep 1
	-docker rmi sudo3

build:
	docker build --no-cache -t sudo3 .

run:
	docker run --rm -v $(CURDIR):/pwd --cap-add=SYS_PTRACE --security-opt seccomp=unconfined -d --name sudo3 -i sudo3

attach:
	docker exec -it sudo3 /bin/bash

root:
	docker exec -u root -it sudo3 /bin/bash
