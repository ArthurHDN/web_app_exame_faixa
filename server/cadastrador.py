from concurrent import futures
import grpc
import cadastrador_pb2
import cadastrador_pb2_grpc


class CadastradorServicer(cadastrador_pb2_grpc.CadastradorServicer):
    def __init__(self):
        print('Instancia Cadastrador Service criada com sucesso' + str(self))

    def Cadastra(self, request, context):
        print('Chamado o metodo de cadastra')
        return cadastrador_pb2.DatabaseResponse(message = 'AAAAAAAAAAA')

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    cadastrador_pb2_grpc.add_CadastradorServicer_to_server(
        CadastradorServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
