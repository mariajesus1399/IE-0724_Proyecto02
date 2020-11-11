# Definimos OS base
FROM ubuntu:20.04
MAINTAINER Ernesto Crespo
RUN apt-get update
RUN apt-get install -y python3-pip
RUN apt-get clean
RUN pip3 install virtualenv
RUN pip3 install django
RUN pip3 install django-widget-tweaks
#RUN echo “America/Venezuela/Caracas” > /etc/timezone && dpkg-reconfigure -f noninteractive tzdata

# El puerto 8000 se publica en el contenedor
EXPOSE 8000

# Copiar aplicacion del subdirectorio djangoapp/ al directorio
# /djangoapp en el contenedor
ADD veterinary /srv/veterinary
COPY veterinary /srv/veterinary
RUN chown -R www-data:www-data /srv/veterinary
RUN chmod a+x /srv/veterinary/manage.py
# Establecer el directorio de trabajo
WORKDIR /srv/veterinary

# Se lanza el servidor web del proyecto django
CMD python3 manage.py runserver 0.0.0.0:8000
