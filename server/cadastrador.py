from concurrent import futures
import grpc
import cadastrador_pb2
import cadastrador_pb2_grpc

from mysqlapi import MySQLAPI


class CadastradorServicer(cadastrador_pb2_grpc.CadastradorServicer):
    def __init__(self):
        print('Instancia Cadastrador Service criada com sucesso' + str(self))
        self._mysql = MySQLAPI('bancodedados', 'didynDB', 'root', 'didyn')

    def Cadastra(self, request, context):
        print('Chamado o metodo de cadastra')
        table = 'cadastro'
        fields = ('nome','gub')
        values = (request.Nome,request.GUB)
        self._mysql.insert(table, fields, values)
        return cadastrador_pb2.DatabaseResponse(message = 'OK')

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    cadastrador_pb2_grpc.add_CadastradorServicer_to_server(
        CadastradorServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
