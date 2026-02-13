class FrequencyTracker:

    def __init__(self):
        self.my_dicti = defaultdict(int)
        self.frequency = defaultdict(set)
        
    def add(self, number: int) -> None:

        old_freq = self.my_dicti[number]
        self.my_dicti[number] = self.my_dicti.get(number, 0) + 1
        new_freq = self.my_dicti[number]
        if old_freq > 0:
            self.frequency[old_freq].discard(number)
            if len(self.frequency[old_freq]) == 0:
                del self.frequency[old_freq]
        self.frequency[new_freq].add(number)
        
    
    def deleteOne(self, number: int) -> None:
        
        if number in self.my_dicti :    
            old_freq = self.my_dicti[number]
            self.frequency[old_freq].discard(number)
            if len(self.frequency[old_freq]) == 0:
                del self.frequency[old_freq]
            self.my_dicti[number] -= 1
            new_freq = self.my_dicti[number]
            if new_freq > 0:
                self.frequency[new_freq].add(number)
            else:
                del self.my_dicti[number]
        
    def hasFrequency(self, frequency: int) -> bool:
        if frequency in self.frequency :
                return True
        return False
           

# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)