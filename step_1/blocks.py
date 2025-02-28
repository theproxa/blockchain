import hashlib  # Для вычисления хэша


class Block():
    def __init__(self, index, previous_hash, data, timestamp, nonce = 0):
        self.index = index
        self.previous_hash = previous_hash
        self.data = data
        self.nonce = nonce
        self.timestamp = timestamp
        self.hash = self.calculate_hash()
    
    def calculate_hash(self):
        block_string = f"{self.index}{self.previous_hash}{self.data}{self.timestamp}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def main_block(self, difficalt):
        target = "0" * difficalt
        while self.hash[:difficalt] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()
