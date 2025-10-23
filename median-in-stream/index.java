import java.util.ArrayList;
import java.util.Arrays;

class GfG {

    static ArrayList<Double> getMedian(int[] arr) {
        ArrayList<Double> res = new ArrayList<>();
        res.add((double) arr[0]);
        for (int i = 1; i < arr.length; i++) {
            int j = i - 1;
            int num = arr[i];
            while (j >= 0 && arr[j] > num) {
                arr[j + 1] = arr[j];
                j--;
            }
            arr[j + 1] = num;

            int len = i + 1;
            double median;
            if (len % 2 != 0) {
                median = arr[len / 2];
            } else {
                median = (arr[(len / 2) - 1] + arr[len / 2]) / 2.0;
            }

            res.add(median);
        }

        return res;
    }

    public static void main(String[] args) {
        int[] arr = { 5, 15, 1, 3, 2, 8 };
        ArrayList<Double> res = getMedian(arr);

        for (int i = 0; i < res.size(); i++) {
            System.out.printf("%.2f ", res.get(i));
        }
    }
}