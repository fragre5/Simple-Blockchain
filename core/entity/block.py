import hashlib

class Block:
    ENCODING = 'utf-8'
    TARGET_PREFIX = '0'
    GENESIS_PREV_HASH = '0'

    def __init__(self, timestamp: float, data: str, previous_hash: str) -> None:
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0

    @property
    def get_hash(self) -> str:
        head = f"{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(head.encode(self.ENCODING)).hexdigest()

    def mine(self, difficulty: int) -> None:
        target = self.TARGET_PREFIX * difficulty
        while self.get_hash[:difficulty] != target:
            self.nonce += 1
