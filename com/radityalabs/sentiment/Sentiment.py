import os

class Sentiment:
    def __init__(self):
        self.path = os.path.expanduser("~/PycharmProjects/FinalSentimentAnalysis/com/radityalabs/sentiment/data")

    def load_review_collection(self):
        with open(self.path + "/review_collection.txt", "r", encoding="utf-8") as f:
            read = f.read().splitlines()
            for row in read:
                print(row)


sentiment = Sentiment()
sentiment.load_review_collection()
