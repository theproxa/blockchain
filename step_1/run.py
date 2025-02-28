from blocks import *
from blockchain import *

# Пример использования
blockchain = Blockchain(difficalt = 1)
blockchain.add_block("First Block")
blockchain.add_block("Second Block")
blockchain.add_block("Third Block")

# Выводим цепочку блоков
for block in blockchain.chain:
    print(f"Block {block.index} [Hash: {block.hash}, Previous Hash: {block.previous_hash}]")

# Проверяем валидность цепочки
print("Is blockchain valid?", blockchain.is_chain_valid())