import json
from uuid import uuid4
from ecdsa import SigningKey, SECP256k1, VerifyingKey

class Transaction:
    def __init__(self, sender, sender_private_key, receiver, amount):
        """
        Конструктор транзакции.
        :param sender: Адрес отправителя.
        :param receiver: Адрес получателя.
        :param amount: Сумма транзакции.
        """
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.id = str(uuid4()) 
        self.signature = self.sign_transaction(sender_private_key)

    def to_dict(self):
        """
        Возвращает транзакцию в виде словаря.
        :return: Словарь с данными транзакции.
        """
        return {
            "id": self.id,
            "sender": self.sender,
            "receiver": self.receiver,
            "amount": self.amount,
            "signature": self.signature
        }

    def sign_transaction(self,private_key):

        transaction_data = {
            "id": self.id,
            "sender": self.sender,
            "receiver": self.receiver,
            "amount": self.amount
        }
        transaction_data_butes = json.dumps(transaction_data, sort_keys=True).encode()

        signing_key = SigningKey.from_string(bytes.fromhex(private_key), curve=SECP256k1)
        signature = signing_key.sign(transaction_data_butes)
        return signature.hex()

    def is_valid(self):
        """
        Проверяет, является ли транзакция валидной.
        :return: True, если подпись верна, иначе False.
        """
        if self.sender == "Genesis":  
            return True
        transaction_data = {
            "id": self.id,
            "sender": self.sender,
            "receiver": self.receiver,
            "amount": self.amount
        }
        
        transaction_data_butes = json.dumps(transaction_data, sort_keys=True).encode()
        
        try:
            verifying_key = VerifyingKey.from_string(bytes.fromhex(self.sender), curve=SECP256k1)
        except ValueError:
            print("Ошибка: Невозможно создать VerifyingKey из публичного ключа.")
            return False


        try:
            return verifying_key.verify(bytes.fromhex(self.signature), transaction_data_butes)
        except:
            return False

    def __repr__(self):
        """
        Возвращает строковое представление транзакции.
        :return: Строка с данными транзакции.
        """
        return json.dumps(self.to_dict(), indent=4)
