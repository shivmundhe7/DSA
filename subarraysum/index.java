import java.util.*;

public class Solution {
    public static int[] subarraySum(int[] arr, int target) {
        int n = arr.length;
        int start = 0;
        int currSum = 0;

        for (int end = 0; end < n; end++) {
            currSum += arr[end];
            while (currSum > target && start <= end) {
                currSum -= arr[start];
                start++;
            }
            if (currSum == target) {
                return new int[] { start + 1, end + 1 }; // 1-based indices
            }
        }
        return new int[] { -1 };
    }

    public static void main(String[] args) {
        int[] arr = { 1, 2, 3, 7, 5 };
        int target = 12;

        int[] result = subarraySum(arr, target);
        System.out.println(Arrays.toString(result));
    }
}
