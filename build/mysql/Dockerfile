FROM mysql:5.6

## Enable mysql connector
# RUN apt-get update -y
# RUN apt-get install mono-devel -y
# RUN apt-get install unzip -y

# RUN mkdir -p /data
# COPY build/bancodedados/mysql-connector-net-8.0.27-noinstall.zip /data
# WORKDIR /data
# RUN unzip mysql-connector-net-8.0.27-noinstall.zip
# WORKDIR /data/net5.0/
# RUN gacutil /i MySql.Data.dll
# WORKDIR /

VOLUME [ "/var/lib/mysql" ]
EXPOSE 3390

ENV MYSQL_ROOT_PASSWORD didyn
ENV MYSQL_ROOT_HOST %
# ENV MYSQL_USER didyn
# ENV MYSQL_PASSWORD didyn
# ENV MYSQL_DATABASE didynDB

ADD build/mysql/*.sql .
RUN chmod 755 *.sql
RUN /etc/init.d/mysql start && \
    mysql -uroot < init_db.sql
