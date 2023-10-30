"""
 Test Scenario 1:
- This function should be able to take a valid URL string as input, with or without the "http" or "https" protocol prefixes.

Test Scenario 2:
- If the URL string does not include the "http" or "https" protocol prefixes, the function should append "https://" to the beginning of the URL string.

Test Scenario 3:
- If the URL string does include the "http" or "https" protocol prefixes, the function should not append "https://" to the URL string.

Test Scenario 4:
- This function should return the time that it took to load the webpage as a float value.

Test Scenario 5:
- The function should return a higher load time value for larger webpages, and lower load times for smaller webpages.

Test Scenario 6:
- When providing the function with an invalid URL, the function should return an exception.

Test Scenario 7:
- If the provided URL leads to a 404 page, the function should still return the time it took to load the 404 error page. 

Test Scenario 8:
- Function should be capable of handling URLs that redirect to another URL.

Test Scenario 9: 
- The function should return 0 if the URL loads instantly. 

Test Scenario 10: 
- The function should handle the URLs with special characters. 

Test Scenario 11: 
- The function should return the correct time even for the URLs which require buffering. 
"""

import unittest
from time_to_load_website import get_load_time
from unittest.mock import patch, MagicMock
from urllib.error import URLError

class TestGetLoadTime(unittest.TestCase):
    @patch('urllib.request.urlopen')
    @patch('time.time')
    def test_valid_url_with_http_https(self, mock_time, mock_urlopen):
        mock_time.side_effect = [12345678.1, 12345678.5]
        get_load_time('https://www.google.com')
        mock_urlopen.assert_called_once_with('https://www.google.com')
        self.assertEqual(get_load_time('https://www.google.com'), 0.4)

    @patch('urllib.request.urlopen')
    @patch('time.time')   
    def test_valid_url_without_http_https(self, mock_time, mock_urlopen):  
        mock_time.side_effect = [12345678.1, 12345678.5]
        get_load_time('www.google.com')
        mock_urlopen.assert_called_once_with('https://www.google.com')
        self.assertEqual(get_load_time('www.google.com'), 0.4)

    def test_invalid_url(self):
        with self.assertRaises(URLError):
            get_load_time('invalid url')  

    @patch('urllib.request.urlopen')
    @patch('time.time')
    def test_404_error_page(self, mock_time, mock_urlopen):
        mock_time.side_effect = [12345678.1, 12345678.5]
        mock_urlopen.side_effect = URLError('Not Found')
        with self.assertRaises(URLError):
            get_load_time('www.error.com') 
            
    @patch('urllib.request.urlopen')
    @patch('time.time')
    def test_url_redirect(self, mock_time, mock_urlopen):
        mock_time.side_effect = [12345678.1, 12345678.9]
        resp = MagicMock()
        resp.url = "www.redirected.com"
        mock_urlopen.return_value = resp
        self.assertEqual(get_load_time('www.original.com'), 0.8)

    @patch('urllib.request.urlopen')
    @patch('time.time')
    def test_loads_instantly(self, mock_time, mock_urlopen):
        mock_time.side_effect = [12345678.1, 12345678.1]
        self.assertEqual(get_load_time('www.instant.com'), 0)
        
    def test_url_with_special_chars(self):
        self.assertIsInstance(get_load_time('https://www.example.com/~user'), float)

    @patch('urllib.request.urlopen')
    @patch('time.time')
    def test_url_requires_buffering(self, mock_time, mock_urlopen):
        mock_time.side_effect = [12345678.1, 12345679.1]
        self.assertEqual(get_load_time('www.buffer.com'), 1)

if __name__ == '__main__':
    unittest.main(verbosity=2)
