package Sprint_01;
import java.util.Scanner;

public class PROBLEM_36 {
    public static void main(String[] args) {

        Scanner kb=new Scanner(System.in);
        int num;
        System.out.println("Enter the number");
        num=kb.nextInt();

        int sum=0;

        for(int i=1;i<=num;i++){
            sum=sum+i;
        }

        System.out.println("The N-th triangular number is "+sum );
    }
}