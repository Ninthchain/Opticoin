from hashlib import sha256


class Hashing:
    @staticmethod
    def make_block_hash(block_id: int, previous_block_hash: str, transactions_hash: str, difficulty=4):
        raise NotImplementedError()

    @staticmethod
    def make_transaction_hash():
        raise NotImplementedError()
