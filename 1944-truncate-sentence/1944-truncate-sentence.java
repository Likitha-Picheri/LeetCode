class Solution {
    public String truncateSentence(String s, int k) {
        String[] arr=s.split(" ");
        String so="";
        int i=0;
        while(k>0){
            so+=arr[i];
            if(k!=1){
               so+=" ";
            }
            i+=1;
            k-=1;

        }
        return so;
    }
}