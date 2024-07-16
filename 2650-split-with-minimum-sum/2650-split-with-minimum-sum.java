class Solution {
    public int splitNum(int num) {
        String s=String.valueOf(num);
        int[] num2= new int[s.length()];
        for(int i=0;i<s.length();i++){
              num2[i]=Character.getNumericValue(s.charAt(i));
        }
        Arrays.sort(num2);
        int[] nums3={0,0};
        for(int i=0;i<num2.length;i++){
            nums3[i%2]=nums3[i%2]*10+num2[i];
        }
        return nums3[0]+nums3[1];
    }
}