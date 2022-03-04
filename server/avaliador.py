from concurrent import futures
import grpc
import avaliador_pb2
import avaliador_pb2_grpc

from mysqlapi import MySQLAPI


class AvaliadorServicer(avaliador_pb2_grpc.AvaliadorServicer):
    def __init__(self):
        self._mysql = MySQLAPI('bancodedados', 'didynDB', 'root', 'didyn')


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    avaliador_pb2_grpc.add_AvaliadorServicer_to_server(
        AvaliadorServicer(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
