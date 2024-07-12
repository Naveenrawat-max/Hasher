import hashlib
import huepy
import argparse
import os
import threading
import sys
import time


def banner():
    a=r'''
_    _           _               
| |  | |         | |              
| |__| | __ _ ___| |__   ___ _ __ 
|  __  |/ _` / __| '_ \ / _ \ '__|
| |  | | (_| \__ \ | | |  __/ |   
|_|  |_|\__,_|___/_| |_|\___|_|   

            Tool by Naveen Rawat                      

'''
    print(huepy.bold(huepy.blue(a)), end="")



def crack(hash_value, hash_type, wordlist_path):
    found = False  # Start with assuming the hash is not found

    try:
        with open(wordlist_path, "r", errors="ignore") as f:
            for word in f:
                word = word.strip()
                hash_object = hashlib.new(hash_type)
                hash_object.update(word.encode())

                if hash_object.hexdigest() == hash_value:
                    print('\n', end="")
                    print(huepy.good(huepy.red("Hash cracked: ")), hash_value)  # Print "Hash cracked:" in red
                    print(huepy.good(huepy.green("Password found: ")), word)  # Print "Password found:" in green
                    found = True
                    break  # Exit the loop if the hash is found

    except KeyboardInterrupt:
        print("\nCtrl+C detected, exiting...")
        sys.exit()
        found = True  # Set found to True to exit the function

    except UnicodeDecodeError:
        # Handle decoding errors gracefully
        print(f"Error decoding word: {word}")

    return found  # Return whether the hash was found or not


if __name__ == "__main__":
    banner()
    parser = argparse.ArgumentParser(description='Hash Cracker')
    parser.add_argument('-hs', '--hash', type=str, help='Hash value to crack')
    parser.add_argument('-a', '--algorithm', type=str, help='Hash algorithm (e.g., md5, sha1)')
    parser.add_argument('-w', '--wordlist', type=str, help='Path to the wordlist file', default='rockyou1.txt')
    parser.add_argument('-all', action='store_true', help='Print all available hash algorithms')

    args = parser.parse_args()

    if args.all:
        print(huepy.good("Supported hash algorithms:"))
        for algorithm in hashlib.algorithms_available:
            print(algorithm , end=" ")
        print('\n')
        exit()

    if not args.hash or not args.algorithm:
        print("Error: Both hash value and algorithm must be specified.")
        exit(1)

    hash_value = args.hash
    hash_type = args.algorithm
    wordlist_path = args.wordlist

    start_time = time.time()

    # Use a thread to perform the cracking
    print(huepy.good('Starting the cracking process'))
    time.sleep(1)
    print(huepy.good('Fetching all the passwords from wordlist'))
    crack_thread = threading.Thread(target=crack, args=(hash_value, hash_type, wordlist_path))
    crack_thread.start()

    # Wait for the thread to finish
    crack_thread.join()

    end_time = time.time()
    ex_time = end_time - start_time
    print(huepy.good(f'Total time taken: {ex_time:.2f}s'), "\n")