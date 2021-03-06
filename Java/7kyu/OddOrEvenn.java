public class OddOrEvenn {
    public static String oddOrEven(int[] array) {
        int x = 0;
        for (int i = 0; i < array.length; i++) {
            x += array[i];
        }
        if (x % 2 == 0) {
            return "even";
        } else {
            return "odd";
        }
    }
}
