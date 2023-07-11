from hashlib import sha256


class Transaction:
    id: int
    value: int
    sender: str
    receiver: str
    hash: str

    def __init__(self, transaction_id, transaction_sender, transaction_receiver, value):
        self.id = transaction_id
        self.sender = transaction_sender
        self.receiver = transaction_receiver
        self.value = value
        self.hash = sha256(str(int(self.receiver + self.sender + self.id + self.value)).encode()).hexdigest()

    def get_id(self) -> int:
        return self.id

    def get_value(self) -> int:
        return self.id

    def get_sender(self) -> str:
        return self.sender

    def get_receiver(self) -> str:
        return self.receiver

    def get_hash(self) -> str:
        return self.hash
