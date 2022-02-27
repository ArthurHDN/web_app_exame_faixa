from concurrent import futures
import grpc
import cadastrador_pb2
import cadastrador_pb2_grpc

from mysqlapi import MySQLAPI


class CadastradorServicer(cadastrador_pb2_grpc.CadastradorServicer):
    def __init__(self):
        self._mysql = MySQLAPI('bancodedados', 'didynDB', 'root', 'didyn')

    def CadastraEscola(self, request, context):
        table = 'escola'
        fields = ('nome','endereco')
        values = (request.nome, request.endereco)
        id = self._mysql.insert(table, fields, values)
        return cadastrador_pb2.DatabaseResponse(message = 'Inserido com ID = ' + str(id))

    def CadastraAluno(self, request, context):
        table = 'aluno'
        fields = ('id_escola', 'nome', 'gub', 'professor')
        values = (request.escola.id, request.nome, request.gub, request.professor)
        id = self._mysql.insert(table, fields, values)
        return cadastrador_pb2.DatabaseResponse(message = 'Inserido com ID = ' + str(id))

    def ListaEscola(self, request, context):
        pass

    def RemoveEscola(self, request, context):
        pass

    def RemoveAluno(self, request, context):
        pass

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    cadastrador_pb2_grpc.add_CadastradorServicer_to_server(
        CadastradorServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
