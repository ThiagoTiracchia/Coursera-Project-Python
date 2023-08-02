from EmotionDetection.emotion_detection import emotion_predictor
import unittest


class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        result_1 = emotion_predictor('I am glad this happened')
        self.assertEqual(result_1, 'joy')
        result_2 = emotion_predictor('I am really mad about this')
        self.assertEqual(result_2, 'anger')
        result_3 = emotion_predictor('I feel disgusted just hearing about this')
        self.assertEqual(result_3, 'disgust')
        result_3 = emotion_predictor('I am so sad about this')
        self.assertEqual(result_3, 'sadness')
        result_3 = emotion_predictor('I am really afraid that this will happen')
        self.assertEqual(result_3, 'fear')


unittest.main()