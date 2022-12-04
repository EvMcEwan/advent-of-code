import hashlib

first_five = ""
counter = 0

while first_five != "000000":
    key = "ckczppom"
    key = key + str(counter)

    result = hashlib.md5(key.encode())

    hex_ = result.hexdigest()
    first_five = hex_[0:6]

    if first_five == "000000":
        print("The answer is " + str(counter))
        print("The hash is ckczppom" + str(counter))
        print("The hexadecimal hash is " + str(hex_))

    counter += 1
