import hashlib

def test_block_initialization(genesis_block):
    assert genesis_block.data == "Genesis"
    assert genesis_block.previous_hash == "0"
    assert genesis_block.nonce == 0

def test_hash_calculation(genesis_block):
    expected_hash = hashlib.sha256(
        f"{genesis_block.timestamp}Genesis0{genesis_block.nonce}"
        .encode('utf-8')
    ).hexdigest()
    assert genesis_block.hash == expected_hash

def test_mine_method(mined_block):
    assert mined_block.hash.startswith("00")
    assert mined_block.nonce > 0

def test_hash_change_on_data_modification(genesis_block):
    original_hash = genesis_block.hash
    genesis_block.data = "Modified"
    assert genesis_block.hash != original_hash
