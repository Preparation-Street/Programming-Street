package Sprint_01;

import java.util.Scanner;

public class PROBLEM_28 {
    public static void main(String[] args) {

        Scanner kb=new Scanner(System.in);
        int num;
        System.out.println("Enter number");
        num=kb.nextInt();
        int fact=1;
        for(int i=num;i>=1;i--){
            fact=i*fact;
        }
        int sum=0;
        while(fact>0){
            sum=sum+fact%10;
            fact=fact/10;
        }
        System.out.println("Sum of factorial is: "+(sum));
    }
}
