import unittest
from models import sources

Sources = sources.Source

class SourceTest(unittest.TestCase):
    '''
    Test class to test behaviour of the source class
    '''
    def setUp(self):
        '''
        Method to run before every Test
        '''
        self.new_source= Sources( "abc-news","ABC News","Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.","http://abcnews.go.com","general")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,sources))

if __name__ == '__main__':
    unittest.main()
