def num_to_hex(num):
    hex_num = hex(num)[2:]
    return hex_num
def hex_to_num(hex_str):
    return int(hex_str, 16)
def binary_to_hex(bin_str):
    return hex(int(bin_str, 2))[2:]
def binary_to_num(bin_str):
    return int(bin_str, 2)
def hex_to_bin(hex_str):
    return bin(int(hex_str, 16))[2:]

print(num_to_hex(255))
print(hex_to_num("CB"))
print(binary_to_hex("00101111"))
print(binary_to_num("00101111"))
print(hex_to_bin("A5"))

