FROM ubuntu:14.04

MAINTAINER 2tom <tera1215@gmail.com>

RUN apt-get update && apt-get install -y\
 software-properties-common\
 curl\
 unzip\
 libcurl4-openssl-dev\
 && rm -rf /var/lib/apt/lists/*

RUN add-apt-repository ppa:webupd8team/java

RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections
RUN apt-get update && apt-get install -y\
 oracle-java8-installer\
 oracle-java8-set-default\
 && rm -rf /var/lib/apt/lists/*

ENV KBN_PKG_NAME kibana-4.1.2-linux-x64

RUN curl -O https://download.elasticsearch.org/kibana/kibana/$KBN_PKG_NAME.tar.gz\
 && tar xfz $KBN_PKG_NAME.tar.gz\
 && rm $KBN_PKG_NAME.tar.gz\
 && mv $KBN_PKG_NAME /opt/kibana

EXPOSE 5601

ADD ./start.sh /start.sh
RUN chmod +x /start.sh
CMD ["/start.sh"]

#CMD ["/opt/kibana/bin/kibana", "-e", "http://$ELASTIC_PORT_9200_TCP_ADDR:$ELASTIC_PORT_9200_TCP_PORT"]
