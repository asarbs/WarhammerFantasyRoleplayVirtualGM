FROM debian

USER root
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y python3 python3-django python3-pip git meld


EXPOSE 3000