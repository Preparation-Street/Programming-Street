package Sprint_01;
import java.util.Scanner;

public class PROBLEM_33 {
    public static void main(String[] args) {

        Scanner kb=new Scanner(System.in);
        int base;
        System.out.println("Enter the base");
        base=kb.nextInt();

        int expo;
        System.out.println("Enter the exponent");
        expo=kb.nextInt();

        int multi=1;

        for(int i=1;i<=expo;i++){
            multi=multi*base;
        }

        System.out.println(multi);
    }
}
