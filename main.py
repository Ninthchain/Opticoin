from queue import Queue
from typing import List

from opticoin.block.structures import Block
from opticoin.block.types import Transaction


class Blockchain:
    @property
    def last_block(self):
        return self.chain[-1]

    def __init__(self):
        self.chain = list()
        self.unconfirmed_transactions = list()
        self.transactions = list()
        self.create_genesis_block()

    def create_genesis_block(self) -> None:
        genesis_block = Block(0, "0000000000000000000000000000000000000000000000000000000000000000", [])
        self.chain.append(genesis_block)

    def add_block(self) -> None:
        previous_block = self.chain[len(self.chain) - 1]
        new_block = Block(previous_block.id, previous_block.hash, self.transactions)
        self.chain.append(new_block)

    def add_new_transaction(self, transaction: Transaction):
        self.transactions.append(transaction)

    def mine(self):
        # Но блокчейн ещё в стадии разработки!!!!
        raise NotImplementedError()


brouhaha = Blockchain()

brouhaha.add_new_transaction(Transaction(0, "asdas", "informatics", 2800))

for block in brouhaha.chain:
    print(block.id, block.transactions)
    for element in block.merkle_tree.get_iterable():
        print(element)

