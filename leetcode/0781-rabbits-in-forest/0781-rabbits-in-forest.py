class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        minRabbits = 0
        dictRabbits = {}

        for ans in answers:
            dictRabbits[ans] = dictRabbits.get(ans, 0) + 1
        
        for ele in dictRabbits:
            if dictRabbits[ele] <= (ele + 1):
                minRabbits += ele + 1
            else:
                minRabbits += math.ceil(dictRabbits[ele]/(ele+1)) * (ele + 1)
                
        return minRabbits