import unittest
import requests
from mock import mock, Mock
from githubAPI import display

class TestGitHubAPI(unittest.TestCase):

    @mock.patch('requests.get')
    def testRichkempinski(self, fake_get):
        fake_response = [Mock(), Mock(), Mock(), Mock(), Mock()]
        fake_response[0].json.return_value = [{'name': 'hellogitworld'}, {'name': 'helloworld'}, {'name': 'Project1'},\
            {'name': 'threads-of-life'}]
        fake_response[1].json.return_value = [{'commit': 2},{'commit': 3}]
        fake_response[2].json.return_value = [{'commit': 2}, {'commit': 3}, {'commit':6}]
        fake_response[3].json.return_value = [{'commit': 2},{'commit': 3}]
        fake_response[4].json.return_value = [{'commit': 2}, {'commit': 3}, {'commit':6}]
        fake_get.side_effect = fake_response

        self.assertEqual(display("richkempinski"),[('hellogitworld', 2), ('helloworld', 3), ('Project1', 2), ('threads-of-life', 3)])

    @mock.patch('requests.get')
    def testLoliveto(self, fake_get):
        fake_response = [Mock(), Mock(), Mock(), Mock(), Mock(), Mock(), Mock(), Mock(), Mock()]
        fake_response[0].json.return_value = [{'name': 'cuddly-fiesta'}, {'name':'D6Project'},\
            {'name':'GitHubApi567'}, {'name':'HW01triangles'}, {'name':'newD6'}, {'name':'SSW322-Project'},\
            {'name':'SSW567HelloWorld'}, {'name':'Triangle567'}]
        fake_response[1].json.return_value = [{"commit": 2}]
        fake_response[2].json.return_value = [{"commit": 2}, {"commit": 2}, {"commit": 2}, {"commit": 2}, {"commit": 2},\
        {"commit": 2}, {"commit": 2}, {"commit": 2}]
        fake_response[3].json.return_value = [{"commit": 2}, {"commit": 2}, {"commit": 2}, {"commit": 2}, {"commit": 2}]
        fake_response[4].json.return_value = [{"commit": 2}, {"commit": 2}, {"commit": 2}, {"commit": 2}, {"commit": 2}, {"commit": 2}]
        fake_response[5].json.return_value = [{"commit": 2}, {"commit": 2}, {"commit": 2}]
        fake_response[6].json.return_value = [{"commit": 2}, {"commit": 2}, {"commit": 2}]
        fake_response[7].json.return_value = [{"commit": 2}, {"commit": 2}, {"commit": 2}, {"commit": 2}, {"commit": 2}, {"commit": 2}]
        fake_response[8].json.return_value = [{"commit": 2}]
        fake_get.side_effect = fake_response
        self.assertEqual(display("loliveto"),[('cuddly-fiesta', 1), ('D6Project', 8),\
            ('GitHubApi567', 5), ('HW01triangles', 6), ('newD6', 3), ('SSW322-Project', 3), ('SSW567HelloWorld', 6), ('Triangle567', 1)])

    @mock.patch('requests.get')
    def testNhilden1114(self, fake_get):
        fake_response = [Mock(), Mock(), Mock(), Mock(), Mock(), Mock()]
        fake_response[0].json.return_value = [{"name": '567-hw1'}, {"name": '567-hw2a'}, {"name": '567githubAPI'},\
            {"name": 'GEDCOMProject'}, {"name": 'SSW567'}]
        fake_response[1].json.return_value = [{"commit": 2},{"commit": 3},{"commit": 3},{"commit": 3}]
        fake_response[2].json.return_value = [{"commit": 2},{"commit": 3}]
        fake_response[3].json.return_value = [{"commit": 2},{"commit": 3},{"commit": 3},{"commit": 3},{"commit": 3},{"commit": 3},\
            {"commit": 3},{"commit": 3}]
        fake_response[4].json.return_value = [{"commit": 2}]
        fake_response[5].json.return_value = [{"commit": 2}]
        fake_get.side_effect = fake_response
        self.assertEqual(display("nhilden1114"), [('567-hw1', 4), ('567-hw2a', 2), ('567githubAPI', 8), ('GEDCOMProject', 1), ('SSW567', 1)])


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
