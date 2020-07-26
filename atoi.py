




class Solution:
    def myAtoi(self, str: str) -> int:
        queue = []
        for e in str:
            result = ord(e) - ord('0')
            if result >= 1 and result <= 9:
                # is a digit
                queue.append(result)
            elif e == '-' and queue == []:
                queue.append(e)
            # is not a digit
            elif queue != []:
                # shouldnt continue
                break
        
        integer = 0
        neg = False
        counter = 0
        if (queue[0] == '-'):
            neg = True
            counter = 1
        while counter < len(queue):
            digit = queue[counter]
            integer = integer * 10
            integer += digit 
            counter += 1
            
        if neg:
            integer =integer - integer * 2 
        return integer
        
    
if __name__ == "__main__":
    string = '              42.asdad'
    print(Solution.myAtoi(string))
                
            
                

            
            
            