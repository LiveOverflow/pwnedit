.PHONY : all stop build run attach root
all : stop build run

stop:
	-docker stop sudo4
	sleep 1
	-docker rmi sudo4

build:
	docker build --no-cache -t sudo4 .

run:
	docker run --rm -v $(CURDIR):/pwd --cap-add=SYS_PTRACE --security-opt seccomp=unconfined -d --name sudo4 -i sudo4

attach:
	docker exec -it sudo4 /bin/bash

root:
	docker exec -u root -it sudo4 /bin/bash
