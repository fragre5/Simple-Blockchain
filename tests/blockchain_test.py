from core.entity.blockchain import Blockchain

def test_blockchain_initialization(sample_blockchain):
    chain = sample_blockchain.chain
    assert len(chain) == 1
    assert chain[0].data == "Genesis block"
    assert chain[0].previous_hash == "0"


def test_add_block(sample_blockchain):
    sample_blockchain.add_block("Test Data")
    assert len(sample_blockchain.chain) == 2
    assert sample_blockchain.chain[1].data == "Test Data"


def test_block_linking(sample_blockchain):
    sample_blockchain.add_block("Block 1")
    sample_blockchain.add_block("Block 2")

    block1 = sample_blockchain.chain[1]
    block2 = sample_blockchain.chain[2]

    assert block1.previous_hash == sample_blockchain.chain[0].get_hash
    assert block2.previous_hash == block1.get_hash


def test_chain_validation(sample_blockchain):
    sample_blockchain.add_block("Valid Data")
    assert sample_blockchain.is_chain_valid() is True


def test_tamper_detection(sample_blockchain):
    sample_blockchain.add_block("Original Data")
    sample_blockchain.chain[1].data = "Tampered Data"
    assert sample_blockchain.is_chain_valid() is False


def test_empty_chain_validation(sample_blockchain):
    assert sample_blockchain.is_chain_valid() is True


def test_different_difficulty_levels():
    blockchain = Blockchain(difficulty=2)
    blockchain.add_block("Test")
    assert blockchain.chain[1].get_hash.startswith("00")
