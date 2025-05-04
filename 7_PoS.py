# 7. Write a program in Python to implement PoS consensus algorithm. 

# Consider Thyself as a Validator (According to the book)
import hashlib
import datetime

class Block:
    def __init__(self, block_number, data, previous_hash):
        self.block_number = block_number
        self.timestamp = datetime.datetime.now()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()
    
    def calculate_hash(self):
        data_string = str(self.block_number) + str(self.timestamp) + str(self.data) + str(self.previous_hash)
        return hashlib.sha256(data_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
    
    def create_genesis_block(self):
        return Block(0, "Genesis Block", "0")
    
    def get_latest_block(self):
        return self.chain[-1]
    
    def add_block(self, new_block):
        self.chain.append(new_block)


    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

    def print_chain(self):
        for block in self.chain:
            print(f"Block Number: {block.block_number}")
            print(f"Timestamp: {block.timestamp}")
            print(f"Data: {block.data}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Hash: {block.hash}")
            print("-" * 50)


if __name__ == "__main__":
    blockchain = Blockchain()

    block1 = Block(1, "Transaction 1", blockchain.get_latest_block().hash)
    blockchain.add_block(block1)
    block2 = Block(2, "Transaction 2", blockchain.get_latest_block().hash)
    blockchain.add_block(block2)
    block3 = Block(3, "Transaction 3", blockchain.get_latest_block().hash)
    blockchain.add_block(block3)

    blockchain.print_chain()
    print(f"Is the blockchain valid? {blockchain.is_chain_valid()}")

    # Tampering Data
    block1.data = "Transaction 10"
    blockchain.print_chain()
    print(f"Is the blockchain valid? {blockchain.is_chain_valid()}")


# Actual Proof of Stack Implementation
# import hashlib
# import random
# import time

# class Block:
#     def __init__(self, index, previous_hash, timestamp, data, validator):
#         self.index = index
#         self.previous_hash = previous_hash
#         self.timestamp = timestamp
#         self.data = data
#         self.validator = validator
#         self.hash = self.calculate_hash()

#     def calculate_hash(self):
#         value = (str(self.index) + self.previous_hash +
#                  str(self.timestamp) + str(self.data) + self.validator)
#         return hashlib.sha256(value.encode('utf-8')).hexdigest()

#     def __str__(self):
#         return f"Block #{self.index} by {self.validator}: {self.hash}"

# class Blockchain:
#     def __init__(self):
#         self.chain = [self.create_genesis_block()]
#         self.validators = {}

#     def create_genesis_block(self):
#         return Block(0, "0", time.time(), "Genesis Block", "Network")

#     def get_last_block(self):
#         return self.chain[-1]

#     def add_validator(self, name, stake):
#         self.validators[name] = stake

#     def select_validator(self):
#         total_stake = sum(self.validators.values())
#         pick = random.uniform(0, total_stake)
#         current = 0
#         for validator, stake in self.validators.items():
#             current += stake
#             if current > pick:
#                 return validator
#         return random.choice(list(self.validators.keys()))  # fallback

#     def add_block(self, data):
#         validator = self.select_validator()
#         last_block = self.get_last_block()
#         new_block = Block(
#             index=last_block.index + 1,
#             previous_hash=last_block.hash,
#             timestamp=time.time(),
#             data=data,
#             validator=validator
#         )
#         self.chain.append(new_block)
#         print(f"Block added by {validator}.")

#     def is_chain_valid(self):
#         for i in range(1, len(self.chain)):
#             current = self.chain[i]
#             previous = self.chain[i - 1]

#             if current.hash != current.calculate_hash():
#                 return False

#             if current.previous_hash != previous.hash:
#                 return False
#         return True

#     def print_chain(self):
#         for block in self.chain:
#             print(block)

# # --- Example Usage ---

# if __name__ == "__main__":
#     blockchain = Blockchain()

#     # Add validators
#     blockchain.add_validator("Alice", stake=50)
#     blockchain.add_validator("Bob", stake=30)
#     blockchain.add_validator("Charlie", stake=20)

#     # Add some blocks
#     blockchain.add_block("First block after genesis")
#     blockchain.add_block("Second block after genesis")
#     blockchain.add_block("Third block after genesis")

#     # Display the blockchain
#     blockchain.print_chain()

#     # Check if valid
#     print("Blockchain valid?", blockchain.is_chain_valid())
