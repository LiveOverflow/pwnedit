.PHONY : all stop build run attach root
all : stop build run

stop:
	-docker stop sudo11
	sleep 1
	-docker rmi sudo11

build:
	docker build --no-cache -t sudo11 .

run:
	docker run --rm -v $(CURDIR):/pwd --cap-add=SYS_PTRACE --security-opt seccomp=unconfined -d --name sudo11 -i sudo11

attach:
	docker exec -it sudo11 /bin/bash

root:
	docker exec -u root -it sudo11 /bin/bash
