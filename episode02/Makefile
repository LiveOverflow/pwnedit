.PHONY : all stop build run attach root
all : stop build run

stop:
	-docker stop sudo2
	sleep 1
	-docker rmi sudo2

build:
	docker build --no-cache -t sudo2 .

run:
	docker run --rm -v $(CURDIR):/pwd --cap-add=SYS_PTRACE --security-opt seccomp=unconfined -d --name sudo2 -i sudo2

attach:
	docker exec -it sudo2 /bin/bash

root:
	docker exec -u root -it sudo2 /bin/bash
