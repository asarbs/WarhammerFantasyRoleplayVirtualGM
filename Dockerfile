FROM debian

USER root
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y python3 python3-django python3-pip git meld python3-bs4 pipx
RUN rm -f /usr/lib/python3.x/EXTERNALLY-MANAGED
RUN pip3 install requests django-static-jquery --break-system-packages

EXPOSE 3000