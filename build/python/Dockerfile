FROM ubuntu:focal AS python_base
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
    python3 \
    python3-pip 

RUN pip3 install --upgrade pip
RUN pip3 install grpcio 
RUN pip3 install grpcio-tools
RUN pip3 install mysql-connector-python


######################################
FROM python_base AS python_cadastrador
ADD server/cadastrador.py .
ADD server/testcadastrador.py .
ADD server/mysqlapi.py .
RUN python3 -m grpc_tools.protoc -Iprotos --python_out=. --grpc_python_out=. protos/cadastrador.proto

ENTRYPOINT [ "python3", "cadastrador.py" ]


######################################
FROM python_base AS python_avaliador
ADD server/avaliador.py .
ADD server/testavaliador.py .
ADD server/mysqlapi.py .
RUN python3 -m grpc_tools.protoc -Iprotos --python_out=. --grpc_python_out=. protos/avaliador.proto

ENTRYPOINT [ "python3", "avaliador.py" ]
