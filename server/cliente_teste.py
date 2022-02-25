import grpc
import cadastrador_pb2
import cadastrador_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = cadastrador_pb2_grpc.CadastradorStub(channel)
        print(stub.Cadastra(cadastrador_pb2.Aluno()))

if __name__ == '__main__':
    run()
    