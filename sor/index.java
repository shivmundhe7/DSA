import java.util.Arrays;

class Geeks {
    public static void main(String args[]) {
       
        int[] a = { 2, -1, 3, 4 };
      
        char[] b = { 'b', 'a', 'c', 'b' };
        
        Arrays.sort(a);
        Arrays.sort(b);
        System.out.print("");
        for (int n : a) {
            System.out.print(n + " ");
        }
        
        System.out.print("\n");
        for (char c : b) {
            System.out.print(c + " ");
        }
    }
}