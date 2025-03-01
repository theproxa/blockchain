import hashlib  # Для вычисления хэша
import json

class Block():
    def __init__(self, index, previous_hash, transection, timestamp, nonce = 0):
        self.index = index
        self.previous_hash = previous_hash
        self.transection = transection
        self.nonce = nonce
        self.timestamp = timestamp
        self.hash = self.calculate_hash()
    
    def calculate_hash(self):
        block_string = json.dumps({
            "index": self.index,
            "previous_hash": self.previous_hash,
            "transactions": [tx.to_dict() for tx in self.transection],
            "timestamp": self.timestamp,
            "nonce": self.nonce
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def main_block(self, difficalt):
        target = "0" * difficalt
        while self.hash[:difficalt] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()

    def __repr__(self):

        return json.dumps({
            "index": self.index,
            "previous_hash": self.previous_hash,
            "transactions": [tx.to_dict() for tx in self.transection],
            "timestamp": self.timestamp,
            "nonce": self.nonce,
            "hash": self.hash
        }, indent=4)