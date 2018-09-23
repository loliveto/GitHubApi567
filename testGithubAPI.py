import unittest

from githubAPI import display

class TestGitHubAPI(unittest.TestCase):
    def testRichkempinski(self):
        self.assertEqual(display("richkempinski"),[('hellogitworld', 30), ('helloworld', 2), ('Project1', 2), ('threads-of-life', 1)])

    def testLoliveto(self):
        self.assertEqual(display("richkempinski"),[('cuddly-fiesta', 1), ('D6Project', 8), ('GitHubApi567', 5), ('HW01triangles', 6), ('newD6', 30), ('SSW322-Project', 30), ('SSW567HelloWorld', 6), ('Triangle567', 10)])

    def testNhilden1114(self):
        self.assertEqual(display("nhilden1114"), [('567-hw1', 4), ('567-hw2a', 12), ('567githubAPI', 8), ('GEDCOMProject', 18), ('SSW567', 1)])

    def testCfenollosa(self):
        self.assertEqual(display("cfenollosa"), [('aekii', 20), ('bashblog', 30), ('calmerge', 2), ('chatbot_pybcn', 2), ('dsl-libretto50ct', 2), ('eu-cookie-law', 2), ('feedtube', 2), ('NotesAppExport', 2), ('os-tutorial', 2)])