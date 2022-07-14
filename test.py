import unittest
import index
import json


class Testing(unittest.TestCase):
    def setUp(self):

        fn = open('sample_newsapi.json')
        data_newsapi = json.load(fn)
        fn.close()

        f = open('sample_reddit.json')
        data_reddit = json.load(f)
        f.close()

        self.newsapi_processor_response =  index.proccess_newsapi_response(data_newsapi['articles'])
        self.reddit_processor_response =  index.proccess_reddit_response(data_reddit['data']['children'])

        self.newsapi_response_get_latest = index.search_newsapi()
        self.reddit_response_get_latest = index.search_reddit_news()

        self.newsapi_response_search = index.search_newsapi("game")
        self.reddit_response_search = index.search_reddit_news("game")

        self.newsapi_api_response_get_latest = index.get_latest_news()
        self.newsapi_api_response_search = index.get_news_by_topic("game")

    def test_newsapi_proccessor_is_list(self):
        self.assertEqual(type(self.newsapi_processor_response), list)

    def test_newsapi_proccessor_is_not_empty(self):
        self.assertNotEqual(len(self.newsapi_processor_response), 0)

    def test_newsapi_proccessor_contains_source(self):
        self.assertTrue("source" in self.newsapi_processor_response[0])
    def test_newsapi_proccessor_contains_link(self):
        self.assertTrue("link" in self.newsapi_processor_response[0])
    def test_newsapi_proccessor_contains_headline(self):
        self.assertTrue("headline" in self.newsapi_processor_response[0])

    def test_reddit_proccessor_is_list(self):
        self.assertEqual(type(self.reddit_processor_response), list)

    def test_reddit_proccessor_is_not_empty(self):
        self.assertNotEqual(len(self.reddit_processor_response), 0)

    def test_reddit_proccessor_contains_source(self):
        self.assertTrue("source" in self.reddit_processor_response[0])
    def test_reddit_proccessor_contains_link(self):
        self.assertTrue("link" in self.reddit_processor_response[0])
    def test_reddit_proccessor_contains_headline(self):
        self.assertTrue("headline" in self.reddit_processor_response[0])

    def test_newsapi_response_is_list(self):
        self.assertEqual(type(self.newsapi_response_get_latest), list)
    def test_reddit_response_is_list(self):
        self.assertEqual(type(self.reddit_response_get_latest), list)
    
    def test_newsapi_search_response_is_list(self):
        self.assertEqual(type(self.newsapi_response_search), list)
    def test_reddit_search_response_is_list(self):
        self.assertEqual(type(self.reddit_response_search), list)

    def test_reddit_api_get_response_is_list(self):
        self.assertEqual(type(self.newsapi_api_response_get_latest), list)
    def test_newsapi_api_search_response_is_list(self):
        self.assertEqual(type(self.newsapi_api_response_search), list)

if __name__ == '__main__':
    unittest.main()