package Sprint_01;
import java.util.Scanner;

public class PROBLEM_08 {

    public static void main(String[] args) {

        Scanner kb = new Scanner(System.in);
        int a;
        System.out.println("Enter the number");
        a = kb.nextInt();

        int fact = 1;
        for (int i = a; i > 0; i--) {
            fact = fact * i;
        }

        System.out.println("The factorial of given no. is " + fact);
    }
}
