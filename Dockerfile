FROM debian




USER root
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y bash
RUN apt-get install -y bash-completion
RUN apt-get install -y python3
RUN apt-get install -y python3-django
RUN apt-get install -y python3-pip
RUN apt-get install -y git
RUN apt-get install -y python3-bs4
RUN apt-get install -y pipx
RUN rm -f /usr/lib/python3.x/EXTERNALLY-MANAGED
RUN pip3 install requests django-static-jquery django-autocomplete-light django-tinymce django-tables2 --break-system-packages

SHELL ["/bin/bash", "-c"]

EXPOSE 3000