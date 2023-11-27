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
RUN apt-get install -y sqlite3
RUN apt-get install -y sqlite3
RUN rm -f /usr/lib/python3.x/EXTERNALLY-MANAGED
RUN pip3 install --break-system-packages requests
RUN pip3 install --break-system-packages django-static-jquery
RUN pip3 install --break-system-packages django-autocomplete-light
RUN pip3 install --break-system-packages django-tinymce
RUN pip3 install --break-system-packages django-tables2
RUN pip3 install --break-system-packages django-ajax-selects
RUN pip3 install --break-system-packages pillow
RUN pip3 install --break-system-packages django-allauth

SHELL ["/bin/bash", "-c"]

EXPOSE 3000