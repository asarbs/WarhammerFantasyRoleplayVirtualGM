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
RUN apt-get install -y nodejs 
RUN apt-get install -y npm
RUN apt-get install -y wget

RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get install -y ./google-chrome-stable_current_amd64.deb


RUN rm -f /usr/lib/python3.x/EXTERNALLY-MANAGED
RUN pip3 install requests --break-system-packages
RUN pip3 install django-static-jquery --break-system-packages
RUN pip3 install django-autocomplete-light --break-system-packages
RUN pip3 install django-tinymce --break-system-packages
RUN pip3 install django-tables2 --break-system-packages
RUN pip3 install django-ajax-selects --break-system-packages
RUN pip3 install 'channels[daphne]' --break-system-packages
RUN pip3 install channels_redis --break-system-packages
RUN pip3 install pillow --break-system-packages
RUN pip3 install django-request --break-system-packages
RUN pip3 install google-api-python-client --break-system-packages
RUN pip3 install djangorestframework --break-system-packages
RUN pip3 install markdown --break-system-packages
RUN pip3 install django-filter --break-system-packages
RUN pip3 install feedparser --break-system-packages
RUN pip3 install selenium --break-system-packages
RUN pip3 install webdriver-manager --break-system-packages
RUN pip3 install social-auth-app-django --break-system-packages


#RUN npm install @owlbear-rodeo/sdk

SHELL ["/bin/bash", "-c"]

EXPOSE 3000