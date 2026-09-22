import random

def encode():
    og_key = int(input("key: "))
    random_range_start = int(input("range start: "))
    random_range_end = og_key

    key = random.randint(random_range_start, random_range_end)

    buffed_key = og_key * key
    result = str(buffed_key) + str(key) + str(len(str(key)))

    print("\n--- ENCODED ---")
    print("buffed key:", buffed_key)
    print("key:", key)
    print("final result:", result)


def decode():
    encoded = input("encoded value: ")

    # Last digit = length of the random key
    key_len = int(encoded[-1])

    # Remove length digit
    encoded_without_length = encoded[:-1]

    # Extract random key
    key = int(encoded_without_length[-key_len:])

    # Extract buffed key
    buffed_key = int(encoded_without_length[:-key_len])

    # Recover original key
    if buffed_key % key != 0:
        print("Invalid encoded value.")
        return

    og_key = buffed_key // key

    print("\n--- DECODED ---")
    print("original key:", og_key)
    print("random key:", key)
    print("buffed key:", buffed_key)


while True:
    print("\n1. Encode")
    print("2. Decode")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        encode()
    elif choice == "2":
        decode()
    elif choice == "3":
        break
    else:
        print("Invalid choice.")
