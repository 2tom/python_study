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

ENV ES_PKG_NAME elasticsearch-1.7.1

RUN curl -L -O https://download.elastic.co/elasticsearch/elasticsearch/$ES_PKG_NAME.tar.gz\
 && tar xvzf $ES_PKG_NAME.tar.gz\
 && rm -f $ES_PKG_NAME.tar.gz\
 && mv $ES_PKG_NAME /opt/elasticsearch

RUN printf "path.data: /data\n" >> /opt/elasticsearch/config/elasticsearch.yml\
 && printf "path.logs: /dev/fd/1\n" >> /opt/elasticsearch/config/elasticsearch.yml\
 && printf "path.work: /data/work\n" >> /opt/elasticsearch/config/elasticsearch.yml\
 && printf "action.destructive_requires_name: true\n" >> /opt/elasticsearch/config/elasticsearch.yml\
 && printf "index.refresh_insterval: 10s\n" >> /opt/elasticsearch/config/elasticsearch.yml\
 && printf "bootstrap.mlockall: true\n" >> /opt/elasticsearch/config/elasticsearch.yml

RUN cd /tmp\
 && curl -O http://download.elasticsearch.org/elasticsearch/elasticsearch-analysis-kuromoji/elasticsearch-analysis-kuromoji-2.7.0.zip\
 && /opt/elasticsearch/bin/plugin -u file:///tmp/elasticsearch-analysis-kuromoji-2.7.0.zip --install elasticsearch/elasticsearch-analysis-kuromoji/2.7.0\
 && rm -f elasticsearch-analysis-kuromoji-2.7.0.zip\
 && curl -O https://codeload.github.com/mobz/elasticsearch-head/zip/master\
 && /opt/elasticsearch/bin/plugin -u file:///tmp/master --install mobz/elasticsearch-head\
 && rm -f master\
 && curl -O https://codeload.github.com/polyfractal/elasticsearch-inquisitor/zip/master\
 && /opt/elasticsearch/bin/plugin -u file:///tmp/master --install polyfractal/elasticsearch-inquisitor\
 && rm -f master


RUN  mkdir -p /data
VOLUME ["/data"]
EXPOSE 9200
EXPOSE 9300

ENTRYPOINT ["/opt/elasticsearch/bin/elasticsearch"]
