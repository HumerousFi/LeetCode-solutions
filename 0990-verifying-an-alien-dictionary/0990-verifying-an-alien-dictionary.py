class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {val : i for i, val in enumerate(order)}
        # print(order_map)
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            for j in range(min(len(word1), len(word2))):
                if order_map[word1[j]] < order_map[word2[j]]:
                    break
                elif order_map[word1[j]] > order_map[word2[j]]:
                    return False
            else:
                if len(word1) > len(word2):
                    return False

        return True
