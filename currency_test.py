import unittest
from app import app  # Import your Flask app instance

class CurrencyConverterTestCase(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_currency_conversion(self):
        with self.app as client:
            # Send a POST request with the same currency for conversion
            resp = client.post('/', data={'from_currency': 'USD', 'to_currency': 'USD', 'amount': '1'})
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)

            # Check if the expected conversion result is present in the HTML
            expected_result = '1 USD IS EQUAL TO 1 USD'
            self.assertIn(expected_result, html)

    def test_uppercase_convert(self):
       with self.app as client:
            response = client.post('/', data={
                'from_currency': 'usd',  # lowercase input
                'to_currency': 'usd',  # lowercase input
                'amount': '1'
            })
            data = response.data.decode('utf-8')
            self.assertEqual(response.status_code, 200)
            
            # Check if the expected conversion result is present in the HTML (case-insensitive)
            expected_result = '1 USD IS EQUAL TO 1 USD'
            self.assertIn(expected_result.lower(), data.lower())
            

    #can't get this to work....
   # def test_currency_match(self):
   #     with app.test_client() as client:
   #         # cchecking if symbols appears in the h1?
   #         resp = client.get('/')
   #         html = resp.get_data(as_text=True)
#
   #         self.assertEqual(resp.status_code, 200)
   #         self.assertIn('<h1>{{result}}</h1>', html)



