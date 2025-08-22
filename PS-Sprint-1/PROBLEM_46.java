package Sprint_01;

public class PROBLEM_46 {
    public static void main(String[] args) {

        String st = "Tarun";

        char[] st1 = st.toCharArray();

        int count = 0;

        for (int i = 0; i < st1.length; i++) {
            count++;
        }

        System.out.println("The length of the given string is " + count);

    }
}
