import unittest
from app import app

class TestCompanyAPI(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_search_endpoint(self):
        response = self.app.get('/company/list?q=solution')
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)

    def test_update_endpoint(self):
        data_to_update = {'description': 'Updated solutions provider test'}
        response = self.app.put('/company/48-factoring-inc', json=data_to_update, content_type='application/json')
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Company updated successfully')

if __name__ == '__main__':
    unittest.main()
