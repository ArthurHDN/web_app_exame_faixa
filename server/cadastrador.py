from concurrent import futures
import grpc
import cadastrador_pb2
import cadastrador_pb2_grpc

from mysqlapi import MySQLAPI, TABLE_ALUNO, TABLE_AVALIACAO, TABLE_ESCOLA


class CadastradorServicer(cadastrador_pb2_grpc.CadastradorServicer):
    
    def __init__(self):
        self._mysql = MySQLAPI('bancodedados', 'didynDB', 'root', 'didyn')

    def CadastraEscola(self, request, context):
        table = TABLE_ESCOLA
        fields = ('nome','endereco')
        values = (request.nome, request.endereco)
        id = self._mysql.insert(table, fields, values)
        return cadastrador_pb2.DatabaseResponse(message = 'Inserido ID = ' + str(id))

    def CadastraAluno(self, request, context):
        table = TABLE_ALUNO
        fields = ('id_escola', 'nome', 'gub', 'professor')
        values = (request.escola.id, request.nome, request.gub, request.professor)
        id = self._mysql.insert(table, fields, values)
        return cadastrador_pb2.DatabaseResponse(message = 'Inserido com ID = ' + str(id))

    def ListaEscola(self, request, context):
        table = TABLE_ESCOLA
        fields = '*'
        for escola in self._mysql.select(table, fields):
            yield cadastrador_pb2.Escola(nome=escola['nome'], endereco=escola['endereco'])

    def ListaAluno(self, request, context):
        table = TABLE_ALUNO
        fields = '*'
        for aluno in self._mysql.select(table, fields):
            yield cadastrador_pb2.Aluno(escola = cadastrador_pb2.ID(id = aluno['id_escola']), nome=aluno['nome'], gub=aluno['gub'], professor=aluno['professor'])

    def RemoveEscola(self, request, context):
        id = request.id
        table = TABLE_ESCOLA
        filter = 'id_escola = ' + str(id)
        self._mysql.delete(table, filter)
        return cadastrador_pb2.DatabaseResponse(message = 'Removido ID = ' + str(id))

    def RemoveAluno(self, request, context):
        id = request.id
        table = TABLE_ALUNO
        filter = 'id_aluno = ' + str(id)
        self._mysql.delete(table, filter)
        return cadastrador_pb2.DatabaseResponse(message = 'Removido ID = ' + str(id))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    cadastrador_pb2_grpc.add_CadastradorServicer_to_server(
        CadastradorServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
