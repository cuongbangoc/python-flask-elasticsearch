from app import app
from config import config as cfg
from flask import jsonify, json

def normalize_search_data(data):
    if data is None:
        return None

    result = {
        'total' : len(data['hits']['hits']),
        'hits' : []
    }

    for hit in data['hits']['hits']:
        result['hits'].append(hit['_source'])

    return result

def is_exists_hit(arr, item):
    return any(x['id'] == item['id'] for x in arr)

def search_by_suggestion(suggest, field, es, index, doc_type):
    body={
        "from": 0,
        "size": 5,
        "sort":[
            {"name": {"order": "asc"}}
        ],
        "query": {
            "match": {field: suggest['text']}
        }
    }

    data = es.search(index, doc_type, body)
    if data is not None:
        return data

    return None

def normalize_search_data_with_suggestion(result, field, es, index, doc_type):
    if result is None:
        return None

    res = {
        'total': 0,
        'hits' : []
    }

    options = []
    for hit in result['hits']['hits']:
        res['hits'].append(hit['_source'])

    for k in result['suggest'].keys():
        suggester = result['suggest'][k]
        if suggester is not None and len(suggester) > 0:
            for suggest in suggester:
                for option in suggest['options']:
                    if option['text'] not in options:
                        # Search with suggestion
                        data = search_by_suggestion(option, field, es, index, doc_type)
                        tmp_hits = []
                        for hit in data['hits']['hits']:
                            if not is_exists_hit(res['hits'], hit['_source']):
                                tmp_hits.append(hit['_source'])

                        res['hits'] = res['hits'] + tmp_hits
                        # Mark suggestion was searched
                        options.append(option['text'])

        res['total'] = len(res['hits'])
    return res