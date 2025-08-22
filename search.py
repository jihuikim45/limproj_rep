import meilisearch

client = meilisearch.Client("http://127.0.0.1:7700", "7-7oWYGNTFBRQX98J3jC7jw3DTYJSw5tBaMvCfYIrEA")

def stock_search(query):
    return client.index('nasdaq').search(query)
