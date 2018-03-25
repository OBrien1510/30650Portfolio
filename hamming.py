import sys

def main():

    precode = sys.argv[1:]
    precode = " ".join(precode)
    postcode = []
    a = 0
    while a < len(precode):
        if precode[a] not in "10":
            print("Error: input sequence should be a sequence of 1's and 0's (illegal character detected")
            exit()
        a += 1
    for i in precode:
        postcode.append(i)

    i = 0
    pos = 2 ** i

    while pos < len(precode) + 1:

        postcode.insert(pos-1, "none")

        i += 1
        pos = 2 ** i

    j = 0
    i = (2**j)

    print("sequence before:",postcode)

    while i - 1 < len(postcode):

        postcode[i - 1] = 0
        x = 0
        index = i-1
        total = 0

        while x < i and index < len(postcode):

            total += int(postcode[index])
            x += 1
            index += 1
            if x == i:
                index = index + i
                x = 0
        postcode[i - 1] = str((total % 2))

        j += 1
        i = (2**j)



    print("".join(postcode))

if __name__ == "__main__":
    main()
