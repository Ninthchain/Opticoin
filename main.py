import math
import random
from _decimal import Decimal
from hashlib import sha256
from queue import Queue
from typing import List

import rsa as rsa

from opticoin.block.structures import Block
from opticoin.block.types import Transaction
from opticoin.blockchain import Blockchain

blockchain = Blockchain()
next_tx_id = 0
for block_id in range(0, 5):
    for _ in range(0, 16):
        tx_data = input().split()
        new_transaction = Transaction(
            transaction_id=next_tx_id,
            transaction_sender=tx_data[0],
            transaction_receiver=tx_data[1],
            value=tx_data[2]
        )
        blockchain.add_new_transaction(new_transaction)
        next_tx_id += 1
    blockchain.add_block()
    blockchain.mine()

for block in blockchain.chain:
    print(f"\nblock number: {block.id}, nonce: {block.nonce}\nmerkle_root: {block.merkle_tree.tree_root}")
    print(f"hash: {block.hash}\n prev_hash: {block.previous_hash}")
    for transaction in block.transactions:
        print(f"transaction number: {transaction.id}, hash: {transaction.hash}")
        print(f"from: {transaction.sender}, to: {transaction.receiver}, value: {transaction.value}")


