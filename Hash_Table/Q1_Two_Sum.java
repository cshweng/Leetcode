import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] twoSum(int[] nums, int target) {
       Map<Integer, Integer> table = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            // System.out.println(i);
            if (table.containsKey(target-nums[i])){
                return new int[] {table.get(target - nums[i]),i};
            } else{
                table.put(nums[i],i);
            }
            }
        return new int[] {}; 
    }
}
