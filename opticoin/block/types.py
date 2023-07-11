from hashlib import sha256


class Transaction:
    id: int
    value: int
    sender: str
    receiver: str
    hash: str
    is_verified: bool

    def __init__(self, transaction_id, transaction_sender, transaction_receiver, value):
        self.id = transaction_id
        self.sender = transaction_sender
        self.receiver = transaction_receiver
        self.value = value
        self.hash = sha256(str(int(self.receiver + self.sender + self.id + self.value)).encode()).hexdigest()
        self.is_verified = False
