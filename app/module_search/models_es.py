from app import es
from app import app
from config import config as cfg
from app.common import elastic as elas
from app.common.helper import normalize_search_data, normalize_search_data_with_suggestion


class User():
    def __init__(self):
        self.es = es
        if self.es is None:
            self.es = elas.Elastic()

    def search_by_name(self, user_name):
        body={
            "from": 0,
            "size": 5,
            "sort":[
                {"name": {"order": "asc"}}
            ],
            "query": {
                "match": {"name": user_name}
            },
            "suggest" : {
                "first_suggestion" : {
                    "text" : user_name,
                    "term" : {
                        "field" : "name"
                    }
                }
            }
        }
        result = self.es.search("clotify", "users", body)
        if result is not None:
            # return normalize_search_data(result)
            return normalize_search_data_with_suggestion(result, "name", self.es, "clotify", "users")

        return None


class Brand():
    def __init__(self):
        self.es = es
        if self.es is None:
            self.es = elas.Elastic()

    def search_by_name(self, brand_name):
        body={
            "from": 0,
            "size": 5,
            "sort":[
                {"name": {"order": "asc"}}
            ],
            "query": {
                "match": {"name": brand_name}
            },
            "suggest" : {
                "first_suggestion" : {
                    "text" : brand_name,
                    "term" : {
                        "field" : "name"
                    }
                }
            }
        }
        result = self.es.search("clotify", "brands", body)
        if result is not None:
            return normalize_search_data(result)

        return None


class Outfit():
    def __init__(self):
        self.es = es
        if self.es is None:
            self.es = elas.Elastic()

    def search_by_name(self, outfit_name):
        body={
            "from": 0,
            "size": 5,
            "sort":[
                {"name": {"order": "asc"}}
            ],
            "query": {
                "match": {"name": outfit_name}
            },
            "suggest" : {
                "first_suggestion" : {
                    "text" : outfit_name,
                    "term" : {
                        "field" : "name"
                    }
                }
            }
        }
        result = self.es.search("clotify", "outfits", body)
        if result is not None:
            #return normalize_search_data(result)
            return normalize_search_data_with_suggestion(result, "name", self.es, "clotify", "outfits")

        return None

    def search_by_tag(self, outfit_tag):
        body={
            "from": 0,
            "size": 5,
            "sort":[
                {"name": {"order": "asc"}}
            ],
            "query": {
                "match": {"tags": outfit_tag}
            },
            "suggest" : {
                "first_suggestion" : {
                    "text" : outfit_tag,
                    "term" : {
                        "field" : "tags"
                    }
                }
            }
        }
        result = self.es.search("clotify", "outfits", body)
        if result is not None:
            return normalize_search_data(result)

        return None


class Offer():
    def __init__(self):
        self.es = es
        if self.es is None:
            self.es = elas.Elastic()

    def search_by_name(self, offer_name):
        body={
            "from": 0,
            "size": 5,
            "sort":[
                {"name": {"order": "asc"}}
            ],
            "query": {
                "match": {"name": offer_name}
            },
            "suggest" : {
                "first_suggestion" : {
                    "text" : offer_name,
                    "term" : {
                        "field" : "name"
                    }
                }
            }
        }
        result = self.es.search("clotify", "offers", body)
        if result is not None:
            return normalize_search_data(result)

        return None
