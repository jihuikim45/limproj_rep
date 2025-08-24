import meilisearch

client = meilisearch.Client("http://127.0.0.1:7700", "1aGotZHbnRC7yfep6MgG_4gCboQFrF2wK33O6_YSQO4")

def stock_search(query):
    return client.index('nasdaq').search(query)
