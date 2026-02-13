class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_count = {}

        for i in range(len(chars)):
            if chars[i] in char_count:
                char_count[chars[i]] += 1
            else:
                char_count[chars[i]] = 1

        total = 0

        for word in words:
            word_count = {}
            good = True

            for ch in word:
                if ch in word_count:
                    word_count[ch] += 1
                else:
                    word_count[ch] = 1

                if ch not in char_count or word_count[ch] > char_count[ch]:
                    good = False
                    break

            if good:
                total += len(word)

        return total
