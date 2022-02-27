FROM ubuntu:focal
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
    python3 \
    python3-pip 

RUN pip3 install --upgrade pip
RUN pip3 install grpcio 
RUN pip3 install grpcio-tools

RUN pip3 install mysql-connector-python

ADD server/ .
RUN python3 -m grpc_tools.protoc -Iprotos --python_out=. --grpc_python_out=. protos/cadastrador.proto

ENTRYPOINT [ "python3", "cadastrador.py" ]
