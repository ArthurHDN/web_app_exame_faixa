import grpc
import cadastrador_pb2
import cadastrador_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = cadastrador_pb2_grpc.CadastradorStub(channel)
        print(stub.CadastraEscola(cadastrador_pb2.Escola(nome='DiomarTKD')))
        print(stub.CadastraAluno(cadastrador_pb2.Aluno(escola = cadastrador_pb2.ID(id = 1), nome='Joaozinm', gub=5, professor='prof')))

if __name__ == '__main__':
    run()
    