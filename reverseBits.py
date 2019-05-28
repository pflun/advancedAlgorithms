class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # convert to bin, zfill(32) because of 32 bits so we need to add several 0s to make it 32 bits
        binary = bin(n)[2:].zfill(32)
        i = 0
        j = len(binary) - 1

        # reverse
        binary = list(binary)
        while i < j:
            binary[i], binary[j] = binary[j], binary[i]
            i += 1
            j -= 1
        binary = "".join(binary)

        # int(x, base=10), convert a (bin/octal/hex) into decimal
        return int(binary, 2)


test = Solution()
print test.reverseBits(43261596)