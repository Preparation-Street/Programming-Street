package Sprint_01;
import java.util.Scanner;

public class PROBLEM_25 {
    public static void main(String[] args) {

        Scanner kb=new Scanner(System.in);
        int num;
        System.out.println("Enter the number to check length");
        num=kb.nextInt();

        int temp=num;
        int length=0;

        while(temp!=0){
            length=length+1;
            temp=temp/10;
        }
        System.out.println("The number has "+length+" digits");
    }
}
