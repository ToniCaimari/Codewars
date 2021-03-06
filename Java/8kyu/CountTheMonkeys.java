public class CountTheMonkeys {

    public static int[] monkeyCount(final int n) {
        int[] list;
        list = new int[n];
        for (int i = 0; i < n; i++) {
            list[i] = i + 1;
        }
        return list;
    }
}
