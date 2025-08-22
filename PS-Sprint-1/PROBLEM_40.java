package Sprint_01;
import java.util.Scanner;

public class PROBLEM_40 {
    public static void main(String[] args) {

        Scanner kb=new Scanner(System.in);
        int num;
        System.out.println("Enter the number: ");
        num=kb.nextInt();

        // Repeat the process until num becomes a single digit
        while(num>=10){

            int sum=0;
            while(num>0){
               int temp1=num%10;
                sum=sum+temp1; // Add last digit
                num=num/10; // remove last digit
            }
            num=sum; // Replace num with the sum of its digits
        }
        System.out.println(num);
    }
}
