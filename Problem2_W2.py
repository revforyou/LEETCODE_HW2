class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxlen, largestCount = 0, 0
        arr = collections.Counter()
        for i in range(len(s)):
            arr[s[i]] += 1
            largestCount = max(largestCount, arr[s[i]])
            if maxlen - largestCount >= k:
                arr[s[i - maxlen]] -= 1
            else:
                maxlen += 1
        return maxlen
