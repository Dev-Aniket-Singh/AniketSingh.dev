class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        characters = set()
        left = 0
        answer = 0

        for right in range(len(s)):
            
            while s[right] in characters:
                characters.remove(s[left])
                left += 1

            characters.add(s[right])

            length = right - left + 1
            answer = max(answer, length)

        return answer