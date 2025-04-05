# from blockchain import Blockchain

# my_blockchain = Blockchain()

# my_blockchain.add_transaction('Alice', 'Bob', 10)
# my_blockchain.add_transaction('Bob', 'Charlie', 5)
# my_blockchain.add_transaction('Charlie', 'Alice', 3)

# previous_block = my_blockchain.get_previous_block()
# previous_proof = previous_block.proof
# new_proof = my_blockchain.proof_of_work(previous_proof)
# previous_hash = previous_block.hash
# my_blockchain.add_transaction('Genesis', 'Miner', 1)
# new_block = my_blockchain.create_block(new_proof, previous_hash)

# for block in my_blockchain.chain:
#     print("Block #", block.index)
#     print("Timestamp: ", block.timestamp)
#     print("Transactions: ", block.transactions)
#     print("Proof: ", block.proof)
#     print("Previous Hash: ", block.previous_hash)
#     print("Hash: ", block.hash)
#     print("-------------------------------------")
    
# print("Is Blockchain Valid:", my_blockchain.is_chain_valid(my_blockchain.chain))

from blockchain import Blockchain

my_blockchain = Blockchain()

# Nhập giao dịch từ bàn phím
while True:
    sender = input("Người gửi (hoặc gõ 'x' để kết thúc): ")
    if sender.lower() == 'x':
        break
    receiver = input("Người nhận: ")
    amount = float(input("Số tiền: "))
    my_blockchain.add_transaction(sender, receiver, amount)
    print("Đã thêm giao dịch!\n")

# Tiến hành tạo khối mới sau khi nhập xong giao dịch
previous_block = my_blockchain.get_previous_block()
previous_proof = previous_block.proof
new_proof = my_blockchain.proof_of_work(previous_proof)
previous_hash = previous_block.hash

# Thêm phần thưởng đào (tuỳ chọn)
my_blockchain.add_transaction('Genesis', 'Miner', 1)

# Tạo khối mới
new_block = my_blockchain.create_block(new_proof, previous_hash)

# In ra toàn bộ blockchain
for block in my_blockchain.chain:
    print("Block #", block.index)
    print("Timestamp: ", block.timestamp)
    print("Transactions: ", block.transactions)
    print("Proof: ", block.proof)
    print("Previous Hash: ", block.previous_hash)
    print("Hash: ", block.hash)
    print("-------------------------------------")

print("Is Blockchain Valid:", my_blockchain.is_chain_valid(my_blockchain.chain))
