public class ANeedleintheHaystack {
    public static String findNeedle(Object[] haystack) {
        String nPosition = "";
        for (int i = 0; i < haystack.length; i++) {
            if (haystack[i] == "needle") {
                nPosition = Integer.toString(i);
            }
        }
        return "found the needle at position " + nPosition;
    }
}