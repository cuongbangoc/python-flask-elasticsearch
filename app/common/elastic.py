from app import app
from elasticsearch import Elasticsearch
from config import config as cfg

class Elastic():
    def __init__(self):
        self.es = None
        self.connect()

    def connect(self):
        try:
            self.es = Elasticsearch(cfg.ELASTIC_HOSTS)
            app.logger.info("Connected Elastic Node : {}".format(cfg.ELASTIC_HOSTS))
        except Exception as e:
            app.logger.error("Could not connect to ElasticSearch")
            app.logger.exception(e)

    def search(self, index, doc_type, body):
        app.logger.info("ES Searching processing")
        res = None
        try:
            res = self.es.search(index=index, doc_type=doc_type, body=body)
            app.logger.info("ES Searching successful")
        except Exception as e:
            app.logger.error("ES Searching Error")
            app.logger.exception(e)

        return res
