class Solution:
    def get_next(self, k, num, recurse=0):
        if (num%10) == (k-1):
            return self.get_next(k, num//10, recurse+1)
        else:
            return (num+1)*(10**recurse) if recurse else (num+1)

    def convert_to_base_10(self, k, num, digits):

        base_10 = 0
        for pos in range(digits):
            base_10 += (k**pos)*(num%10)
            num //= 10
        
        return base_10

    def is_palindrome(self, num):
        
        reverse = 0

        temp = num
        while temp!=0:
            reverse = (reverse*10) + (temp%10)
            temp //= 10

        return num == reverse

    def create_palindrom_num(self, base_num, digits):
        
        if digits%2 == 0:
            second_half = str(base_num)[::-1]
        else:
            second_half = str(base_num)[-2::-1]

        palindrome_base = int(str(base_num) + second_half)

        return palindrome_base

    def kMirror(self, k: int, n: int) -> int:
        digits = 1
        
        palindromes = 0
        sum = 0
        while True:
            if digits%2 == 0:
                end = int(digits/2 - 1)
            else:
                end = int((digits-1)/2)
            
            checks = (k-1)*(k**end)

            base_num = 10**end

            for attempt in range(checks):
                base_10 = self.convert_to_base_10(k, self.create_palindrom_num(base_num, digits), digits)
                
                if self.is_palindrome(base_10):
                    palindromes += 1
                    sum += base_10
            
                if palindromes == n:
                    return sum
                
                base_num = self.get_next(k, base_num)
        
            digits += 1
    
print(Solution().kMirror(k=3, n=7))