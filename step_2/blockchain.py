import time    

from blocks import Block

class Blockchain:

    def __init__(self, difficalt = 1):
        self.chain = [self.create_genesis_block()]
        self.difficalt = difficalt
        self.pading_transaction = []
    
    def create_genesis_block(self):
        return Block(0, "0", [], time.time())
    
    def get_latest_block(self):
        return self.chain[-1]
    
    def add_transaction(self, transaction):
        self.pading_transaction.append(transaction)
    
    def mine_pending_transactions(self):
        previous_block = self.get_latest_block()
        new_block = Block(
            index = previous_block.index + 1,
            previous_hash = previous_block.hash,
            transection = self.pading_transaction,
            timestamp = time.time()
        )
        new_block.main_block(1)
        self.chain.append(new_block)
        self.pading_transaction = []
    
    
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
            
            for tx in current_block.transection:
                if not tx.is_valid():
                    print(f"transaction {tx.id} in block {current_block.index} invailid")
                    return False


        return True