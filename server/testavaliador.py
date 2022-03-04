import unittest
unittest.TestLoader.sortTestMethodsUsing = None

import grpc
import avaliador_pb2
import avaliador_pb2_grpc
from google.protobuf.json_format import MessageToJson


class TestAvaliador(unittest.TestCase):
    
    _stub = None


def run():
    with grpc.insecure_channel('localhost:50052') as channel:
        TestAvaliador._stub = avaliador_pb2_grpc.AvaliadorStub(channel)
        unittest.main()


if __name__ == '__main__':
    run()
    