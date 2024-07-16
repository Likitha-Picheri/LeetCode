class Solution {
    public int minimumSum(int num) {
        String s=String.valueOf(num);
        System.out.println(s);
        int[] nums=new int[4];
        int count=0;
        for(int i=0;i<s.length();i++){
            nums[i]=Character.getNumericValue(s.charAt(i));
            if(nums[i]==0){
                count++;
            }
        }
        Arrays.sort(nums);
        int num3[]= {0,0};
        for(int i=0;i<4;i++){
            if(nums[i]!=0){
                num3[i%2]=(num3[i%2]*10) + nums[i];
            }
        }

        return num3[0]+num3[1];
    }
}