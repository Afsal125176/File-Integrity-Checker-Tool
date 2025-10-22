import hashlib
import os
import json

# File to store original hash values
HASH_RECORD_FILE = "file_hashes.json"

def calculate_hash(file_path):
    """Calculate SHA256 hash of a file."""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def load_hashes():
    """Load previously stored file hashes."""
    if os.path.exists(HASH_RECORD_FILE):
        with open(HASH_RECORD_FILE, "r") as f:
            return json.load(f)
    return {}

def save_hashes(hashes):
    """Save hash records to file."""
    with open(HASH_RECORD_FILE, "w") as f:
        json.dump(hashes, f, indent=4)

def monitor_directory(directory):
    """Monitor directory for file changes."""
    stored_hashes = load_hashes()
    current_hashes = {}

    print("\n--- Scanning directory for changes ---\n")

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = calculate_hash(file_path)
            current_hashes[file_path] = file_hash

            if file_path not in stored_hashes:
                print(f"[NEW] File added: {file_path}")
            elif stored_hashes[file_path] != file_hash:
                print(f"[MODIFIED] File changed: {file_path}")

    for file_path in stored_hashes:
        if file_path not in current_hashes:
            print(f"[DELETED] File removed: {file_path}")

    save_hashes(current_hashes)
    print("\nHash records updated successfully.")

if __name__ == "__main__":
    folder = input("Enter the folder path to monitor: ").strip()
    if os.path.isdir(folder):
        monitor_directory(folder)
    else:
        print("Invalid directory. Please try again.")
