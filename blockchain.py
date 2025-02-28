import time    

from blocks import Block

class Blockchain:

    def __init__(self, difficalt = 1):
        self.chain = [self.create_genesis_block()]
        self.difficalt = difficalt
    
    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block", time.time())
    
    def get_latest_block(self):
        return self.chain[-1]
    
    def add_block(self,data):
        previous_block = self.get_latest_block()
        new_block = Block(
            index = previous_block.index+1,
            previous_hash=previous_block.hash,
            data=data,
            timestamp=time.time(),
        )
        new_block.main_block(self.difficalt)
        self.chain.append(new_block)
    
    def is_chain_valid(self):
        for i in range(1,len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            if current_block.hash != current_block.calculate_hash():
                print("invailid current block hash")
                return False
            
            if current_block.previous_hash != previous_block.hash:
                print("invailid previous block hash")
                return False
        return True