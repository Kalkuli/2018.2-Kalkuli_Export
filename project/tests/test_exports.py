import json
from project.tests.base import BaseTestCase
import unittest


class TestExportService(BaseTestCase):

    def test_exports(self):

        with self.client:

            response = self.client.post(
                '/export',
                data=json.dumps({
                    "receipts": [
                        {
                            "cnpj": "000.000.000/0000-00",
                            "company_id": 1234,
                            "emission_date": "2018-11-10",
                            "emission_place": "place",
                            "id": 1,
                            "tax_value": 123.12,
                            "total_price": 456.45
                        },
                        {
                            "cnpj": "000.000.000/0000-00",
                            "company_id": 1234,
                            "emission_date": "2018-10-10",
                            "emission_place": "place",
                            "id": 2,
                            "tax_value": 123.12,
                            "total_price": 456.45
                        },
                        {
                            "cnpj": "000.000.000/0000-00",
                            "company_id": 1234,
                            "emission_date": "2018-10-12",
                            "emission_place": "place",
                            "id": 3,
                            "tax_value": 123.12,
                            "total_price": 456.45
                        }
                    ],
                    "total_cost": "1369.35"
                }),
                content_type='application/json',
            )

            self.assertEqual(response.status_code, 200)
            
    def test_not_json(self):

            with self.client:

                response = self.client.post(
                    '/export',
                    data=json.dumps({}),
                    content_type='application/json',
                )

                data = json.loads(response.data.decode())

                self.assertEqual(response.status_code, 400)
                self.assertIn('wrong json', data['message'])


if __name__ == '__main__':
    unittest.main()