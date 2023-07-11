from transaction import Transaction
from typing import List
from hashlib import sha256


class MerkleTree:
    hashes: List[List[str]]

    def __init__(self):
        self.hashes = List[List[str]]()

    def plant(self, transactions: List[Transaction]) -> None:
        current_hash_line = List[str]()
        for transaction in transactions:
            current_hash_line.append(transaction.get_hash())

        count = len(transactions)
        offset = 0

        while count > 0:
            self.hashes.append(current_hash_line)
            current_hash_line = list()

            for i in range(0, count - 1, 2):
                current_hash_line.append(
                    self.combine_leaves(
                        transactions[offset + count],
                        transactions[offset + count + 1]
                    )
                )
            offset += count
            count //= 2

    def get_iterable(self) -> List[List[str]]:
        return self.hashes

    def combine_leaves(self, left_leave: str, right_leave: str) -> str:
        return sha256((left_leave + right_leave).encode()).hexdigest()
