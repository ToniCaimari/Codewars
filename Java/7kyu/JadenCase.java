public class JadenCase {

    public String toJadenCase(String phrase) {
        System.out.println(phrase);
        String response = "";
        boolean start = true;
        boolean alert = false;
        if (phrase != null && phrase != "") {
            for (int i = 0; i < phrase.length(); i++) {
                if (start == true) {
                    response += Character.toString(phrase.charAt(i)).toUpperCase();
                    start = false;
                } else if (alert == false && Character.toString(phrase.charAt(i)) != " "
                        || Character.toString(phrase.charAt(i)) != "'") {
                    response += phrase.charAt(i);
                } else if (Character.toString(phrase.charAt(i)) == " " || Character.toString(phrase.charAt(i)) == "'") {
                    response += phrase.charAt(i);
                    alert = true;
                } else if (alert == true) {
                    response += Character.toString(phrase.charAt(i)).toUpperCase();
                    alert = false;
                }
            }
        } else {
            return null;
        }
        return response;
    }
}
