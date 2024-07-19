class Solution {
    public String maxValue(String n, int x) {
        boolean negative =false;
        if(n.charAt(0)=='-'){
            negative=true;
            n=n.substring(1);
        }
        for(int i=0;i<n.length();i++){
            int current=n.charAt(i)-'0';
            if(!negative && current<x || negative && current>x){
                return (negative? "-":"")+n.substring(0,i)+x+n.substring(i);


            }
        }
        return (negative?"-":"")+n+x;
        
        
    }
}