package Sprint_01;

import java.util.Scanner;

class PROBLEM_06 {
    public static void main(String[] args) {

        Scanner kb = new Scanner(System.in);
        String sr;
        System.out.println("Enter the string");
        sr = kb.next();

        String rev = "";

        for (int i = sr.length() - 1; i >= 0; i--) {

            rev = rev + sr.charAt(i);

        }

        if (sr.equalsIgnoreCase(rev)) {
            System.out.println("It is a palindrome");
        } else {
            System.out.println("It is not a palindrome");
        }


    }
}