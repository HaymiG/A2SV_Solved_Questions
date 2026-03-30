class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
      
        skill.sort()
        team_skill = skill[0] + skill[-1]
        chem = skill[0] * skill[-1]
        
        for i in range(1, len(skill) // 2):
            if skill[i] + skill[-1 - i] != team_skill:
                return -1
            chem += skill[i] * skill[-1 - i]
        
        return chem

