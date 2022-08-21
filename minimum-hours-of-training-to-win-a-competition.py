class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        n = len(energy)
        res = 0
        for i in range(n):
            if initialEnergy > energy[i]:
                initialEnergy -= energy[i]
            else:
                res += energy[i] + 1 - initialEnergy
                initialEnergy = 1
            if initialExperience > experience[i]:
                initialExperience += experience[i]
            else:
                res += experience[i] + 1 - initialExperience
                initialExperience = 2 * experience[i] + 1
        return res