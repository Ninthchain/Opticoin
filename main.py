import math
import random
from _decimal import Decimal
from hashlib import sha256
from queue import Queue
from typing import List

import rsa as rsa

from opticoin.block.structures import Block
from opticoin.block.types import Transaction


class Blockchain:

    @property
    def last_block(self):
        return self.chain[-1]

    def __init__(self):
        self.max_transactions = 5
        self.chain = list()
        self.unconfirmed_transactions = list()
        self.transactions = list()
        self.create_genesis_block()

    def create_genesis_block(self) -> None:
        genesis_block = Block(0, "0000000000000000000000000000000000000000000000000000000000000000", [])
        self.chain.append(genesis_block)

    def add_block(self) -> None:
        previous_block = self.chain[len(self.chain) - 1]
        new_block = Block(previous_block.id, previous_block.hash, self.transactions[0: self.max_transactions])
        self.chain.append(new_block)

    def add_new_transaction(self, transaction: Transaction):
        self.transactions.append(transaction)

    def mine(self):
        # Но блокчейн ещё в стадии разработки!!!!
        raise NotImplementedError()


