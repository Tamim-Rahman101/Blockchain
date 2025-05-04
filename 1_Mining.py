# 1. Write a program in Python to implement blockchain.
# 2. Write a program in Python for mining a new block in a blockchain, and print the values of the new block.
# 3. Write a program in Python to create four new blocks in a blockchain. Traverse the blocks and print the values.
# 6. Write a program in Python to implement PoW algorithm.
# 9. Write a Python Program that Takes a String and the Desired Number of Leading Zeros from the User and Outputs the 
#    Input String, the Nonce Value for Which the Leading Zeros Puzzle Is Solved, and the Corresponding Hash Generated 
# 10. Write a program in Python that Demonstrates How to Use the SHA-256 Hash Function and Its Application in a Simple Blockchain
# 12. Write a Python program to Demonstrate a Simple Implementation of a Blockchain Using Hash Codes as a Chain of Blocks
# 13. Write a Python program to Demonstrate the Mining Process in Blockchain 


import hashlib
import datetime

class Block:
    def __init__(self, block_number, data, previous_hash):
        self.block_number = block_number
        self.timestamp = datetime.datetime.now()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    # SHA-256 hash
    def calculate_hash(self):
        data_string = str(self.block_number) + str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(data_string.encode()).hexdigest()
    
    # Proof of Work (PoW) algorithm
    def mine_block(self, difficulty):
        while self.hash[:difficulty] != '0'*difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"Block {self.block_number} minded with hash: {self.hash}")
    
class Blockchain:
    def __init__(self):
        self.difficulty = 4
        self.chain = [self.create_genesis_block()]
        # self.difficulty = int(input("Enter the difficulty: "))

    def create_genesis_block(self):
        genesis = Block(0, "Genesis Block", "0")
        genesis.mine_block(self.difficulty)       # use it for leading zeros (difficulty)
        return genesis
    
    def get_latest_block(self):
        return self.chain[-1]
    
    def add_block(self, new_block):
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)
    
    def print_chain(self):
        for block in self.chain:
            print(f"Block Number: {block.block_number}")
            print(f"Timestamp: {block.timestamp}")
            print(f"Data: {block.data}")
            print(f"Nonce: {block.nonce}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Hash: {block.hash}")
            print("-" * 50)
    
    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

if __name__ == "__main__":
    blockchain = Blockchain()

    # Adding 4 new blocks
    block1 = Block(1, "Block 1", blockchain.get_latest_block().hash)
    blockchain.add_block(block1)
    block2 = Block(2, "Block 2", blockchain.get_latest_block().hash)
    blockchain.add_block(block2)
    block3 = Block(3, "Block 3", blockchain.get_latest_block().hash)
    blockchain.add_block(block3)
    block4 = Block(4, "Block 4", blockchain.get_latest_block().hash)
    blockchain.add_block(block4)

    # Traverse and print the blockchain
    blockchain.print_chain()
    print(f"Is the chain valid? {blockchain.is_chain_valid()}")

    # Changing block data
    block2.data = "Changed"
    blockchain.print_chain()
    print(f"Is the chain valid? {blockchain.is_chain_valid()}")
