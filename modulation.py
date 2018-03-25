import sys

conversion = {"0000": "11110", "0001": "01001", "0010": "10100", "0011": "10101",
              "0100": "01010", "0101": "01011", "0110": "01110", "0111": "01111",
              "1000": "10010", "1001": "10011", "1010": "10110", "1011": "10111",
              "1100": "11010", "1101": "11011", "1110": "11100", "1111": "11101"}


def main():

    precode = sys.argv[1:]
    precode = "".join(precode)
    j = 0
    while j < len(precode):
        if precode[j] not in "10":
            print("Error: input sequence should be a sequence of 1's and 0's (illegal character detected")
            exit()
        j += 1

    if len(precode) % 4 != 0:
        print("Error: input sequence should be represented in bytes (bits of 4)")
        exit()

    postcode = []
    i = 0
    while i < len(precode):
        postcode.append(conversion[precode[i:i+4]])
        i += 4

    print(''.join(postcode))


if __name__ == "__main__":
    main()
