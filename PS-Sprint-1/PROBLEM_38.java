package Sprint_01;
import java.util.Scanner;

public class PROBLEM_38 {
    public static void main(String[] args) {

        Scanner kb=new Scanner(System.in);
        int num;
        System.out.println("Enter the number");
        num=kb.nextInt();

        double sum=0;
        int temp=num;

        while(temp!=0){
            int digit=temp%10;
            sum=sum+Math.pow(digit,2);
            temp=temp/10;
        }

        System.out.println((int)sum);

    }
}
