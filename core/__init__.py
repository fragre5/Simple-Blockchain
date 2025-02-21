from core.entity.blockchain import Blockchain

CHAIN_DIFFICULTY = 5

def test_blockchain_integrity(chain: Blockchain) -> None:
    print("Initial chain valid:", blockchain.is_chain_valid())

    print("\nTampering data . . .")
    if len(chain.chain) > 1:
        chain.chain[1].data = "Hacked data"
        print("After tampering valid:", chain.is_chain_valid())
    else:
        print("Chain too short for tampering")

if __name__ == "__main__":
    blockchain = Blockchain(difficulty=CHAIN_DIFFICULTY)

    blockchain.add_blocks([
        "First transaction: Misha -> Sasha 0.0120001 BTC",
        "Second transaction: Juli -> Karl 0.0000004 BTC",
        "Third transaction: Alice -> Misha 0.5550000 BTC"
    ])

    blockchain.print_chain()
    blockchain.save_to_file()

    test_blockchain_integrity(blockchain)
