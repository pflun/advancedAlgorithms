class Codec:
    # #,# can never occur
    def encode(self, strs):
        """Encodes a list of strings to a single string.
        """
        pre = [s.replace("#", "##") for s in strs]
        pre = [s.replace(",", ",,") for s in pre]
        return "#,#".join(pre)

    def decode(self, s):
        """Decodes a single string to a list of strings.
        """
        k = s.split("#,#")
        k = [r.replace("##", "#") for r in k]
        return [r.replace(",,", ",") for r in k]