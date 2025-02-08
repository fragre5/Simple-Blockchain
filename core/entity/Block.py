import hashlib

class Block:
    ENCODING = 'utf-8'
    TARGET_PREFIX = '0'
    GENESIS_PREV_HASH = '0'

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0

    @property
    def hash(self):
        head = f"{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(head.encode(self.ENCODING)).hexdigest()

    def mine(self, difficulty):
        target = self.TARGET_PREFIX * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
