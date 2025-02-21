import pytest
import time
from core.entity.block import Block
from core.entity.blockchain import Blockchain

@pytest.fixture
def genesis_block():
    return Block(time.time(), "Genesis", "0")

@pytest.fixture
def sample_blockchain():
    return Blockchain(difficulty=4)

@pytest.fixture
def mined_block():
    block = Block(time.time(), "Test", "0")
    block.mine(2)
    return block
