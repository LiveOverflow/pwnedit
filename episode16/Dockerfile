FROM ubuntu:20.04
ENV LC_CTYPE C.UTF-8
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -yq gcc make wget curl git vim gdb clang llvm lld llvm-dev bsdmainutils libstdc++-10-dev python3 python3-pip python3-dev automake flex bison build-essential libglib2.0-dev libpixman-1-dev python3-setuptools libffi-dev libssl-dev
#RUN cd /root/ && wget https://www.sudo.ws/dist/sudo-1.8.31p2.tar.gz && tar -xvf sudo-1.8.31p2.tar.gz && cd sudo-1.8.31p2 && ./configure && make && make install
ADD sudo-1.8.31p2 /root/sudo-1.8.31p2
RUN cd /root/sudo-1.8.31p2 && ./configure && make && make install
RUN python3 -m pip install --upgrade pip && python3 -m pip install --upgrade pwntools
RUN bash -c "$(curl -fsSL http://gef.blah.cat/sh)"
RUN useradd -ms /bin/bash user
RUN echo 'export PS1="\[\e]0;\u@\h: \w\a\]\[\033[01;31m\]\u\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]# "' >> /root/.bashrc
RUN echo 'export PS1="\[\e]0;\u@\h: \w\a\]\[\033[01;32m\]\u\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]$ "' >> /home/user/.bashrc
USER user
WORKDIR /home/user
