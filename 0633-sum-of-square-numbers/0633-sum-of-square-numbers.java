import java.util.*;
class Solution {
    public boolean judgeSquareSum(int c) {
       int t=(int)Math.floor(Math.sqrt(c));
       for(int i=0;i<=t;i++){
        if((Math.sqrt(c-i*i))==Math.floor(Math.sqrt(c-i*i))){
            return true;
        }
       }
       return false;
    }
}