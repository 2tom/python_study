FROM ubuntu:14.04

MAINTAINER 2tom <tera1215@gmail.com>

RUN apt-get update && apt-get install -y\
 apache2\
 apache2-utils\
 && rm -rf /var/lib/apt/lists/*

ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_PID_FILE /var/run/apache2.pid
ENV APACHE_RUN_DIR /var/run/apache2
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2

EXPOSE 80

# error: Invalid Mutex directory in argument file:/var/lock/apache2
RUN mkdir -p /var/lock/apache2

VOLUME /var/log/apache2

CMD ["/usr/sbin/apache2", "-D", "FOREGROUND"]
