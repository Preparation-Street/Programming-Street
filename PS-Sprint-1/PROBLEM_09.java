package Sprint_01;
import java.util.Scanner;

public class PROBLEM_09 {
    public static void main(String[] args) {

        Scanner kb=new Scanner(System.in);
        int a;
        System.out.println("Enter the number");
        a=kb.nextInt();

        int sum=0;
        while(a!=0){
            sum=sum+a%10;
            a=a/10;
        }

        System.out.println("The sum of the number is "+sum);
    }
}
