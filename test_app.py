import unittest
import json
from app import app, veiculos

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True 
        self.auth_headers = {'Authorization': 'Basic YWRtaW46TVNYMTIz='}  # admin:MSX123

    def test_get_veiculos(self):
        response = self.app.get('/veiculos', headers=self.auth_headers)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)

    def test_create_veiculo(self):
        novo_veiculo = {
            "placa": "TEST123",
            "marca": "TestMarca",
            "fabricante": "TestFabricante",
            "cor": "TestCor",
            "tipo": "TestTipo",
            "combustivel": "TestCombustivel"
        }
        response = self.app.post('/veiculos', 
                                 headers=self.auth_headers,
                                 data=json.dumps(novo_veiculo),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data['placa'], "TEST123")

    def test_get_veiculo(self):
        response = self.app.get('/veiculos/ABC1234', headers=self.auth_headers)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['placa'], "ABC1234")

    def test_update_veiculo_status(self):
        response = self.app.put('/veiculos/ABC1234', 
                                headers=self.auth_headers,
                                data=json.dumps({"status": "CONNECTADO"}),
                                content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], "CONNECTADO")

    def test_delete_veiculo(self):
        response = self.app.delete('/veiculos/ABC1234', headers=self.auth_headers)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data['result'])

    def test_unauthorized_access(self):
        response = self.app.get('/veiculos')
        self.assertEqual(response.status_code, 401)

if __name__ == '__main__':
    unittest.main()