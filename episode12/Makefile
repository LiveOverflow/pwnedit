.PHONY : all stop build run attach root
all : stop build run

stop:
	-docker stop sudo12
	sleep 1
	-docker rmi sudo12

build:
	docker build --no-cache -t sudo12 .

run:
	docker run --rm -v $(CURDIR):/pwd --cap-add=SYS_PTRACE --security-opt seccomp=unconfined -d --name sudo12 -i sudo12

attach:
	docker exec -it sudo12 /bin/bash

root:
	docker exec -u root -it sudo12 /bin/bash
