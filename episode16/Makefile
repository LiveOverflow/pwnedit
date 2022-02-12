.PHONY : all stop build run attach root
all : stop build run

stop:
	-docker stop sudo16
	sleep 1
	-docker rmi sudo16

build:
	docker build --no-cache -t sudo16 .

run:
	docker run --rm -v $(CURDIR):/pwd --cap-add=SYS_PTRACE --privileged --ulimit core=-1 --security-opt seccomp=unconfined -d --name sudo16 -i sudo16

attach:
	docker exec -it sudo16 /bin/bash

root:
	docker exec -u root -it sudo16 /bin/bash
