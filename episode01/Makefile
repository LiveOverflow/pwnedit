.PHONY : all stop build run attach root
all : stop build run

stop:
	-docker stop sudo1
	sleep 1
	-docker rmi sudo1

build:
	docker build --no-cache -t sudo1 .

run:
	docker run --rm -v $(CURDIR):/pwd --cap-add=SYS_PTRACE --security-opt seccomp=unconfined -d --name sudo1 -i sudo1

attach:
	docker exec -it sudo1 /bin/bash

root:
	docker exec -u root -it sudo1 /bin/bash
