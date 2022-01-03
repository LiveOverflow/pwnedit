.PHONY : all stop build run attach root
all : stop build run

stop:
	-docker stop sudo13
	sleep 1
	-docker rmi sudo13

build:
	docker build --no-cache -t sudo13 .

run:
	docker run --rm -v $(CURDIR):/pwd --cap-add=SYS_PTRACE --security-opt seccomp=unconfined -d --name sudo13 -i sudo13

attach:
	docker exec -it sudo13 /bin/bash

root:
	docker exec -u root -it sudo13 /bin/bash
