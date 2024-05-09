from cachetools import TTLCache

"""
Имитация Redis
"""
class FakeDB:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        self.CACHE = dict()
        self.TTLCACHE = TTLCache(maxsize=10, ttl=5)
