class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if(len(hand) % groupSize != 0):
            return False
        hand.sort()
        print(hand)
        
        while(len(hand) !=0):
            l1 = [hand[0]]
            hand.pop(0)
            for i in range(groupSize-1):
                j = l1[-1]
                if (j+1) in hand:
                    l1.append(j+1)
                    hand.remove(j+1)
                else:
                    return False  
            print(l1)         

        return True 