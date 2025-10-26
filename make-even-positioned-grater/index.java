import java.util.*;

public class GfG {
    static ArrayList<Integer> rearrangeArray(ArrayList<Integer> arr) {
        Collections.sort(arr);

        int n = arr.size();
        ArrayList<Integer> result = new ArrayList<>(Collections.nCopies(n, 0));
        int ptr1 = 0, ptr2 = n - 1;

        for (int i = 0; i < n; i++) {
            if ((i + 1) % 2 == 0) {
                result.set(i, arr.get(ptr2--));
            } else {
                result.set(i, arr.get(ptr1++));
            }
        }
        return result;
    }

    public static void main(String[] args) {
        ArrayList<Integer> arr = new ArrayList<>(Arrays.asList(1, 2, 2, 1));
        ArrayList<Integer> res = rearrangeArray(arr);

        for (int num : res) {
            System.out.print(num + " ");
        }
    }
}