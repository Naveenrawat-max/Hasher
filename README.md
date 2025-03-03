# Hash Cracker

This Python script is a simple hash cracker that attempts to find the plain text password corresponding to a given hash value. It uses a wordlist to compare hashes generated from words against the provided hash.

## Features

- Supports various hash algorithms (MD5, SHA1, SHA256, etc.).
- Uses a wordlist for password guessing.
- Implements multithreading for faster cracking.
- Displays a progress bar to track the cracking process.
- Provides colorful output using the `huepy` library.

## Usage

1. **Install Dependencies:**
   ```bash
   pip install huepy tqdm
   ```
2. Clone this repo and move it to the bin folder
3. python Hasher.py -hs <hash_value> -a <algorithm> -w <wordlist_path>

**Arguments:**
```
-hs or --hash: The hash value to crack.
-a or --algorithm: The hash algorithm used (e.g., md5, sha1, sha256, etc..).
-w or --wordlist: The path to the wordlist file (default: rockyou1.txt).
-all: Print all available hash algorithms:
```


**example usage** :- Hasher.py -hs e691cb702f5d25642aa87009ef1948f8 -a md5 -w rockyou1.txt

**Output:-**




![image](https://github.com/user-attachments/assets/7d5d15d8-026c-4c96-b524-b80fff97a607)


