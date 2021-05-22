FROM ubuntu:20.04
ENV LC_CTYPE C.UTF-8
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -yq gcc make wget curl git vim gdb clang llvm python3 python3-pip bsdmainutils
RUN cd /root/ && wget https://www.sudo.ws/dist/sudo-1.8.31p2.tar.gz && tar -xvf sudo-1.8.31p2.tar.gz && cd sudo-1.8.31p2 && ./configure && make && make install
RUN cd /root/ && git clone https://github.com/google/AFL && cd AFL && make && cd llvm_mode && make && cd .. && make install
RUN useradd -ms /bin/bash user
RUN echo 'export PS1="\[\e]0;\u@\h: \w\a\]\[\033[01;31m\]\u\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]# "' >> /root/.bashrc
RUN echo 'export PS1="\[\e]0;\u@\h: \w\a\]\[\033[01;32m\]\u\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]$ "' >> /home/user/.bashrc
USER user
WORKDIR /home/user
