class Solution {
public:
    bool isPalindrome(int x) 
    {
        // Negative numbers are not palindrome
        // Numbers ending with 0 are not palindrome unless the number is 0
        if (x < 0 || (x % 10 == 0 && x != 0)) 
        {
            return false;
        }
        
        int reversedHalf = 0;
        // Reverse half of the number
        while (x > reversedHalf) 
        {
            reversedHalf = reversedHalf * 10 + x % 10;
            x /= 10;
        }
        return x == reversedHalf || x == reversedHalf / 10;
    }
};
