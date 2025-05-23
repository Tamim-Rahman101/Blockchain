# 4. Write a program in Python to implement a blockchain and print 
#    the values of all fields as described in etherscan.io 

import hashlib
import datetime

class Block:
    def __init__(self, block_number, transactions, previous_hash, gas_limit, gas_used, miner):
        self.block_number = block_number
        self.timestamp = datetime.datetime.now()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.gas_limit = gas_limit
        self.gas_used = gas_used
        self.miner = miner
        self.hash = self.calculate_hash()
    
    def calculate_hash(self):
        data_string = str(self.block_number) + str(self.timestamp) + str(self.transactions) + str(self.previous_hash) + str(self.gas_limit) + str(self.gas_used) + str(self.miner)
        return hashlib.sha256(data_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "Genesis Block", "0", 0, 0, "Genesis Miner")
    
    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        self.chain.append(new_block)
    
    def print_chain(self):
        for block in self.chain:
            print("Block Number: ", block.block_number)
            print("Timestamp: ", block.timestamp)
            print("Transactions: ", block.transactions)
            print("Gas Limit: ", block.gas_limit)
            print("Gas Used: ", block.gas_used)
            print("Miner: ", block.miner)
            print("Previous Hash: ", block.previous_hash)
            print("Block Hash: ", block.hash)
            print("-" * 50)
        
blockchain = Blockchain()

block1 = Block(1, "Transaction 1", blockchain.get_latest_block().hash, 10, 5, "Miner 1")
blockchain.add_block(block1)
block2 = Block(2, "Transaction 2", blockchain.get_latest_block().hash, 20, 15, "Miner21")
blockchain.add_block(block2)
block3 = Block(3, "Transaction 3", blockchain.get_latest_block().hash, 50, 40, "Miner 3")
blockchain.add_block(block3)

blockchain.print_chain()