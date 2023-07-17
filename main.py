import time

from opticoin.block.types import Transaction
from opticoin.blockchain import Blockchain

start_time = time.time()

blockchain = Blockchain()

for _ in range(0, 5):
    for tx_id in range(0, 1024):
        data = input().split()
        tx = Transaction(
            tx_id,
            data[0],
            data[1],
            data[2]
        )
        blockchain.add_new_transaction(tx)
    blockchain.add_block()

gen_time = time.time() - start_time


for block in blockchain.chain:
    print(f"Hash: {block.hash}")
    print(f"Block id: {block.id}")
    print(f"Nonce: {block.nonce}")
    print(f"Merkle root: {block.merkle_tree.tree_root}")
    print(f"Previous block hash: {block.previous_hash}")
    for transaction in block.transactions:
        print(transaction)
    print(f"Block generation time: {gen_time}")
