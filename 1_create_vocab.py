BASE_VOCAB = "/home/pham/F5-TTS-Vietnamese/data/Emilia_ZH_EN_pinyin/vocab.txt"
NEW_VOCAB = "/home/pham/F5-TTS-Vietnamese/data/vivoice_p1_100_sample/vocab.txt"

import os

def read_base_vocab(base_vocab_path):
    """Read base vocabulary from file"""
    with open(base_vocab_path, "r", encoding="utf8") as f:
        base_vocab = set(f.read().splitlines())
    return base_vocab

def extract_vocab_from_metadata(metadata_path):
    """Extract vocabulary from metadata.csv file"""
    tokens = set()
    with open(metadata_path, "r", encoding="utf8") as f:
        for line in f:
            # Split on | and take text part
            text = line.strip().split("|")[1]
            # Add each character to tokens set
            tokens.update(text)
    return tokens

def main():
    # Read base vocabulary
    base_vocab = read_base_vocab(BASE_VOCAB)
    
    # Get metadata path from same directory as NEW_VOCAB
    metadata_path = os.path.join(os.path.dirname(NEW_VOCAB), "metadata.csv")
    
    # Extract vocab from metadata
    new_tokens = extract_vocab_from_metadata(metadata_path)
    
    # Find tokens not in base vocab
    missing_tokens = new_tokens - base_vocab
    
    if missing_tokens:
        print("New tokens found:")
        for token in sorted(missing_tokens):
            print(f"  '{token}'")
            
        # Write extended vocab
        all_tokens = sorted(base_vocab | new_tokens)
        with open(NEW_VOCAB, "w", encoding="utf8") as f:
            f.write("\n".join(all_tokens))
        print(f"\nExtended vocab written to: {NEW_VOCAB}")
    else:
        print("No new tokens found")

if __name__ == "__main__":
    main()

