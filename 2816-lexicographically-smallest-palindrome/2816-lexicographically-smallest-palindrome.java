class Solution {
    public String makeSmallestPalindrome(String s) {
        int left=0;
        int right=s.length()-1;
        StringBuilder sb=new StringBuilder(s);
        while(left<=right){
            if(sb.charAt(left)>sb.charAt(right)){
                sb.setCharAt(left,sb.charAt(right));
            
                
            }
            else if(sb.charAt(left)<sb.charAt(right)){
                sb.setCharAt(right,sb.charAt(left));
            }
            left++;
            right--;
        }
        return sb.toString();
        
    }
}