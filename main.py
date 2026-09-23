import random

def encode():

    og_key = int(input("key: "))

    random_key = random.randint(1,og_key)

    buffed_key = og_key * random_key
    random_key_length = str(len(str(random_key)))
    random_key_length_length = str(len(str(len(str(random_key)))))

    result = random_key_length_length + str(buffed_key) + str(random_key) + random_key_length

    # printing
    
    print("\n--- ENCODED ---\n")
    print(f"{og_key:<25} < inputted key")
    print(f"{random_key:<25} < random key")
    print(f"{random_key_length:<25} < random key length (inserted at the rear of the key)")
    print(f"{random_key_length_length:<25} < random key length length (inserted at the head of the key)")
    print(f"{buffed_key:<25} < buffed key")
    print(f"{result:<25} < final result ( format: [RandomKeyLengthLength] [BuffedKey] [RandomKey] [RandomKeyLength] )")
    print("\n--- ENCODED END ---\n")


def decode():
    encoded = input("encoded key: ")

    # First digit = length of RandomKeyLength
    random_key_length_length = int(encoded[0])

    # Extract RandomKeyLength from the rear
    random_key_length = int(
        encoded[-random_key_length_length:]
    )

    # Remove:
    # 1. RandomKeyLengthLength from the head
    # 2. RandomKeyLength from the rear
    encoded_without_length = encoded[
        1:-random_key_length_length
    ]

    # Extract RandomKey
    random_key = int(
        encoded_without_length[-random_key_length:]
    )

    # Extract BuffedKey
    buffed_key = int(
        encoded_without_length[:-random_key_length]
    )

    # Recover original key
    if buffed_key % random_key != 0:
        print("Invalid encoded value.")
        return

    og_key = buffed_key // random_key

    print("\n--- DECODED ---\n")
    print(f"{encoded:<25} < inputted key")
    print(f"{random_key_length_length:<25} < random key length length")
    print(f"{random_key_length:<25} < random key length")
    print(f"{random_key:<25} < random key")
    print(f"{buffed_key:<25} < buffed key")
    print(f"{og_key:<25} < ogiginal key")
    print("\n--- DECODED END ---\n")

while True:
    print("\n1. Encode")
    print("2. Decode")
    print("3. Exit")

    choice = input("Choose: ")

    if choice in ("e""1"):
        encode()
    elif choice in ("d","2"):
        decode()
    elif choice in ("0","3","Q","q"):
        break
    else:
        print("Invalid choice.")
