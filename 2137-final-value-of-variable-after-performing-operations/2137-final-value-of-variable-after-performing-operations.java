class Solution {
    public int finalValueAfterOperations(String[] operations) {
        int sum1=0;
        for(int i=0;i<operations.length;i++){
            if(operations[i].indexOf('+')!=-1){
                sum1++;
            }
            else{
                sum1--;
            }
        }
        return sum1;
    }
}