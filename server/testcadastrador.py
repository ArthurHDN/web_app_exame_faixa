import unittest
unittest.TestLoader.sortTestMethodsUsing = None

import grpc
import cadastrador_pb2
import cadastrador_pb2_grpc
from google.protobuf.json_format import MessageToJson


class TestCadastrador(unittest.TestCase):
    _stub = None
    _academia_diomar = cadastrador_pb2.Escola(nome='Academia Diomar TKD', endereco='Av. Dr. Cincinato Cajado Braga')
    _aluno_joao = cadastrador_pb2.Aluno(escola=cadastrador_pb2.ID(id=1), nome='Joao', gub=5, professor='Petro')

    def testCadastraUmaEscola(self):
        response = self._stub.CadastraEscola(self._academia_diomar)
        print(MessageToJson(response, including_default_value_fields=True))
        self.assertIn('ID = 1', response.message)

    def testListaUmaEscola(self):
        response = self._stub.ListaEscola(cadastrador_pb2.Void())
        primeiraEscola = next(response)
        print(MessageToJson(primeiraEscola, including_default_value_fields=True))
        self.assertEqual(primeiraEscola, self._academia_diomar)

    def testCadastraUmAluno(self):
        response = self._stub.CadastraAluno(self._aluno_joao)
        print(MessageToJson(response, including_default_value_fields=True))
        self.assertIn('ID = 1', response.message)

    def testListaUmAluno(self):
        response = self._stub.ListaAluno(cadastrador_pb2.Void())
        primeiroAluno = next(response)
        print(MessageToJson(primeiroAluno, including_default_value_fields=True))
        self.assertEqual(primeiroAluno, self._aluno_joao)

    def testRemoveUmAluno(self):
        response = self._stub.RemoveAluno(cadastrador_pb2.ID(id=1))
        print(MessageToJson(response, including_default_value_fields=True))
        self.assertIn('ID = 1', response.message)

    def testRemoveUmaEscola(self):
        response = self._stub.RemoveEscola(cadastrador_pb2.ID(id=1))
        print(MessageToJson(response, including_default_value_fields=True))
        self.assertIn('ID = 1', response.message)


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        TestCadastrador._stub = cadastrador_pb2_grpc.CadastradorStub(channel)
        unittest.main()


if __name__ == '__main__':
    run()
    