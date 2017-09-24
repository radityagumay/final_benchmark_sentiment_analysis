import os
import pymysql

class Sentiment:
    def __init__(self):
        self.path = os.path.expanduser("~/PycharmProjects/FinalSentimentAnalysis/com/radityalabs/sentiment/data")

    @staticmethod
    def connection():
        return pymysql.connect(
            host="127.0.0.1",
            user="root", passwd="",
            db="google_play_review"
        )

    # load collection review from text format
    def load_review_collection(self):
        with open(self.path + "/review_collection.txt", "r", encoding="utf-8") as f:
            read = f.read().splitlines()
            collection = []
            for row in read:
                collection.append(row)
            return collection

    def insert_into_database(self):
        collection = self.load_review_collection()
        c = self.connection()
        conn = c
        c = c.cursor()
        for i in collection:
            document = i.split(',')
            try:
                c.execute(
                    """INSERT INTO `review_label_benchmark_with_polarity`
                    (`authorId`, `authorName`, `googleId`, `reviewBody`, `positive`, `negative`, `neutral`, `polarity`, `label`) VALUES
                    (%s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                    (document[0], document[1], document[2], document[3], document[4], document[5], document[6], document[7], document[8])
                )
                conn.commit()
                print("insert data ", document)
            except:
                conn.rollback()
        conn.close()

    # retrieve review data from database
    def load_review_from_database(self):
        c = self.connection()
        c = c.cursor()
        c.execute("SELECT * FROM review_label_benchmark_with_polarity")
        rows = c.fetchall()
        for d in rows:
            print(d)

sentiment = Sentiment()
sentiment.load_review_from_database()
