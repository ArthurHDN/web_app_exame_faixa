from concurrent import futures
import grpc
import avaliador_pb2
import avaliador_pb2_grpc

from mysqlapi import MySQLAPI, TABLE_ALUNO, TABLE_AVALIACAO, TABLE_ESCOLA


class AvaliadorServicer(avaliador_pb2_grpc.AvaliadorServicer):

    def __init__(self):
        self._mysql = MySQLAPI('bancodedados', 'didynDB', 'root', 'didyn')

    def CriaAvaliacao(self, request, context):
        table = TABLE_AVALIACAO
        fields = ('id_aluno', 'mestre')
        values = (request.aluno.id, request.mestre)
        id = self._mysql.insert(table, fields, values)
        return avaliador_pb2.DatabaseResponse(message = 'Inserido ID = ' + str(id))

    def InsereNota(self, request, context):
        table = TABLE_AVALIACAO
        field = request.nome
        value = request.valor
        filter_ = f"id_aluno = {request.aluno.id}"
        rowcount = self._mysql.update(table, field, value, filter_)
        return avaliador_pb2.DatabaseResponse(message = 'Linhas afetadas = ' + str(rowcount))

    def RemoveAvaliacao(self, request, context):
        id = request.id
        table = TABLE_AVALIACAO
        filter = 'id_avaliacao = ' + str(id)
        self._mysql.delete(table, filter)
        return avaliador_pb2.DatabaseResponse(message = 'Removido ID = ' + str(id))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    avaliador_pb2_grpc.add_AvaliadorServicer_to_server(
        AvaliadorServicer(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
