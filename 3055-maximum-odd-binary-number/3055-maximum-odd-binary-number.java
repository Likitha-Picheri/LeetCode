class Solution {
    public String maximumOddBinaryNumber(String s) {
        int no_ones=s.length()-s.replace("1","").length()-1;
        int no_of_zeros=s.length()-s.replace("0","").length();
        StringBuilder t = new StringBuilder();
        for(int i=0;i<no_ones;i++){
                t.append("1");
        }
        for(int i=0;i<no_of_zeros;i++){
                t.append("0");
        }
        t.append("1");
        return t.toString();
    }
}