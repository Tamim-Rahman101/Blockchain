# 14. Write a program in Python to Create a Merkle Tree in Blockchain.
# 15. Write a program in Python to Prove Membership and Non-membership in a Merkle Tree Blockchain.

import hashlib

def calculate_hash(data_item):
    return hashlib.sha256(data_item.encode()).hexdigest()

def print_tree(tree):
    for level in range(len(tree)):
        print(f"Level {level}")
        for node in range(len(tree[level])):
            print(f"    {tree[level][node]}")
        print("")


def build_merkle_tree(data_items):
    if len(data_items) == 0:
        return None
    
    current_level = [calculate_hash(item) for item in data_items]
    tree = [current_level]

    while len(current_level) > 1:
        if len(current_level) % 2 == 1:
            current_level.append(current_level[-1])

        next_level = []
        for i in range(0, len(current_level), 2):
            parent = calculate_hash(current_level[i] + current_level[i+1])
            next_level.append(parent)
        
        tree.append(next_level)
        current_level = next_level

    return tree


def verify_membership(target_hash, tree):
    for level in tree:
        if len(level) == 1:
            break
        if target_hash in level:
            current_index = level.index(target_hash)

            if current_index % 2 == 0:
                sibling_index = current_index + 1
                target_hash = calculate_hash(level[current_index] + level[sibling_index])
            else:
                sibling_index = current_index - 1
                target_hash = calculate_hash(level[sibling_index] + level[current_index])
        else:
            return False

    # target_hash contains the merkle root hash
    return target_hash == tree[-1][0]


if __name__ == "__main__":
    data_items = ["data1", "data2", "data3", "data4", "data5", "data6", "data7"]
    merkle_tree = build_merkle_tree(data_items)
    print("Merkle Root: ", merkle_tree[-1][0])
    print_tree(merkle_tree)

    # Member
    target = "data3"
    target_hash = calculate_hash(target)
    print(f"{target} is a member of the blockchain: {verify_membership(target_hash, merkle_tree)}")

    # Non-Member
    target = "data33"
    target_hash = calculate_hash(target_hash)
    print(f"{target} is a member of the blockchain: {verify_membership(target_hash, merkle_tree)}")
