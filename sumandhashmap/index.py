import java.util.*;

public class LongestSubarraySumK {
    public static int longestSubarrayWithSumK(int[] arr, int k) {
        // Map to store prefix sum and its first occurrence index
        HashMap<Integer, Integer> map = new HashMap<>();
        int prefixSum = 0;
        int maxLen = 0;

        for (int i = 0; i < arr.length; i++) {
            prefixSum += arr[i];

            // Case 1: if subarray from 0 to i has sum k
            if (prefixSum == k) {
                maxLen = i + 1;
            }

            // Case 2: if prefixSum - k seen before
            if (map.containsKey(prefixSum - k)) {
                int len = i - map.get(prefixSum - k);
                maxLen = Math.max(maxLen, len);
            }

            // Store prefixSum if not already stored (to keep earliest index)
            if (!map.containsKey(prefixSum)) {
                map.put(prefixSum, i);
            }
        }
        return maxLen;
    }

    public static void main(String[] args) {
        int[] arr = {10, 5, 2, 7, 1, 9};
        int k = 15;
        System.out.println("Longest Subarray Length = " + longestSubarrayWithSumK(arr, k));
    }
}
