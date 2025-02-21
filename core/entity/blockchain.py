import time
from typing import List

from core.entity.block import Block

class Blockchain:
    def __init__(self, difficulty: int = 4) -> None:
        self.chain: List[Block] = []
        self.difficulty = difficulty
        self.create_genesis_block()

    def create_genesis_block(self) -> None:
        genesis = Block(
            time.time(),
            "Genesis block",
            Block.GENESIS_PREV_HASH
        )
        genesis.mine(self.difficulty)
        self.chain.append(genesis)

    def get_last_block(self) -> Block:
        return self.chain[-1]

    def add_block(self, data: str) -> None:
        previous_hash = self.get_last_block().hash
        new_block = Block(time.time(), data, previous_hash)
        new_block.mine(self.difficulty)

        if new_block.hash[:self.difficulty] != Block.TARGET_PREFIX * self.difficulty:
            raise ValueError("Invalid block hash difficulty")

        self.chain.append(new_block)

    def add_blocks(self, data_list: List[str]) -> None:
        for data in data_list:
            self.add_block(data)

    def is_chain_valid(self) -> bool:
        for i in range(len(self.chain)):
            current_block = self.chain[i]

            target = Block.TARGET_PREFIX * self.difficulty
            if current_block.hash[:self.difficulty] != target:
                return False

            if i > 0:
                previous_block = self.chain[i - 1]
                if current_block.previous_hash != previous_block.hash:
                    return False

        return True

    def save_to_file(self, filename="output.txt") -> None:
        with open(filename, 'w', encoding='utf-8') as f:
            for block in self.chain:
                f.write(
                    f"Data:\t\t{block.data}\n"
                    f"Timestamp:\t{block.timestamp}\n"
                    f"Nonce:\t\t{block.nonce}\n"
                    f"Hash:\t\t{block.hash}\n"
                    f"PrevHash:\t{block.previous_hash}\n"
                    "\n"
                )

    def print_chain(self) -> None:
        for block in self.chain:
            print(
                f"Data:\t\t{block.data}\n"
                f"Timestamp:\t{block.timestamp}\n"
                f"Nonce:\t\t{block.nonce}\n"
                f"Hash:\t\t{block.hash}\n"
                f"PrevHash:\t{block.previous_hash}\n"
                f"{'-'*50}\n"
            )
