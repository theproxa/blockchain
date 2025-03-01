from blocks import *
from blockchain import *
from transection import *

# Пример использования
blockchain = Blockchain(difficalt = 1)

private_key = SigningKey.generate(curve=SECP256k1).to_string().hex()
public_key = SigningKey.from_string(bytes.fromhex(private_key), curve=SECP256k1).verifying_key.to_string().hex()


private_key1 = SigningKey.generate(curve=SECP256k1).to_string().hex()
public_key1 = SigningKey.from_string(bytes.fromhex(private_key1), curve=SECP256k1).verifying_key.to_string().hex()

private_key2 = SigningKey.generate(curve=SECP256k1).to_string().hex()
public_key2 = SigningKey.from_string(bytes.fromhex(private_key2), curve=SECP256k1).verifying_key.to_string().hex()
# Создаем транзакции
transaction1 = Transaction(public_key, private_key, public_key1, 10)
transaction2 = Transaction(public_key1, private_key1, public_key2, 5)

# Добавляем транзакции в блокчейн
blockchain.add_transaction(transaction1)
blockchain.add_transaction(transaction2)

# Майним блок с транзакциями
blockchain.mine_pending_transactions()

# Выводим блокчейн
for block in blockchain.chain:
    print(block)

# Проверяем валидность цепочки
print("Цепочка валидна:", blockchain.is_chain_valid())