import unittest
from reddit_image_downloader.main import extract_post_id, contains_images

class TestRedditImageDownloader(unittest.TestCase):
    
    def test_extract_post_id(self):
        url = 'https://www.reddit.com/r/test/comments/abc123/test_post/'
        self.assertEqual(extract_post_id(url), 'abc123')
        
    def test_contains_images(self):
        class Comment:
            def __init__(self, body):
                self.body = body
        
        comment = Comment('Here is an image https://preview.redd.it/testimage.jpg')
        self.assertTrue(contains_images(comment))
        
        comment = Comment('No image here!')
        self.assertFalse(contains_images(comment))

if __name__ == '__main__':
    unittest.main()
