FROM ubuntu:14.04
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y python
COPY find_host.py /tmp/gen_config.py
RUN chmod +x /tmp/gen_config.py
VOLUME /wwwroot
VOLUME /wwwconfig
WORKDIR /tmp
ENTRYPOINT ./gen_config.py