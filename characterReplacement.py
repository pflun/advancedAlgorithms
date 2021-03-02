# For a window s[l:r+1], if r - l + 1 - max_freq of s[l:r+1] <= k, we can perform
# at most k operation and change it to a string with repeating characters.
class Solution:
    def characterReplacement(self, s, k):
        counts = collections.Counter()
        start = res = 0

        # We use a window ranging from index start to end
        # We only look in characters inside this window and keep track of their counts
        # We can allow up to K chars that are not the most frequent char in our window

        for end in range(len(s)):
            # at each loop, end is shifted to the right
            counts[s[end]] += 1  # we've seen character 's[end]' one more time in the this new window

            # we shift start to the right only if we ran out of replacements
            # we ran out of replacements if (CHARS that are not the most frequent in current window) > k
            # (end - start + 1) is length of our window, because our window range is INCLUSIVE of both ends
            if end - start + 1 - counts.most_common(1)[0][1] > k:
                # since our window will be shifted, we subtract the character that we are shifting away from by 1
                # because it will no longer be in the new window
                counts[s[start]] -= 1
                start += 1  # now shift our window

            # at each window, simply update res if our current window is larger
            res = max(res, end - start + 1)

        return res