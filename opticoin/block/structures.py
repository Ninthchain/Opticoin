from hashlib import sha256
from typing import List

from opticoin.block.types import Transaction


class MerkleTree:
    hashes: List[List[str]]

    def __init__(self):
        self.hashes = list()

    def plant(self, transactions: list) -> None:
        count = len(transactions)
        current_hash_line = list()
        for i in range(0, count):
            current_hash_line.append(transactions[i])
        offset = 0

        self.hashes.insert(0, current_hash_line)

        while count > 0:

            for i in range(0, count - 1, 2):
                current_hash_line.insert(0, self.combine_leaves(offset + count, offset + count + i))

            offset += count
            count //= 2
            self.hashes.insert(0, current_hash_line)
            current_hash_line = list()

    def get_iterable(self) -> List[List[str]]:
        return self.hashes

    def combine_leaves(self, left_leave: str, right_leave: str) -> str:
        return sha256(str(left_leave + right_leave).encode()).hexdigest()


class Block:
    id: int
    nonce: int
    hash: str
    previous_hash: str
    merkle_tree: MerkleTree
    transactions: List[Transaction]

    def __init__(self, block_id: int, previous_block_hash: str, block_transactions: List[Transaction]):
        self.id = block_id
        self.previous_hash = previous_block_hash
        self.transactions = block_transactions
        self.merkle_tree = MerkleTree()
        self.merkle_tree.plant(self.transactions)
        self.nonce, self.hash = self.block_hash_calculation(self.transactions_hash_calculation())

    def transactions_hash_calculation(self):
        transactions_hash = ""
        for transaction in self.transactions:
            transactions_hash += transaction.hash

        return sha256(transactions_hash.encode()).hexdigest()

    def block_hash_calculation(self, transactions_hash, difficulty=4):
        for nonce in range(10 ** 100):
            msg = (str(self.id) + self.previous_hash + transactions_hash + str(nonce)).encode()

            block_hash = sha256(msg).hexdigest()

            if block_hash.startswith(difficulty * '0'):
                return nonce, block_hash
