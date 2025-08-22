package Sprint_01;

import java.util.Scanner;

public class PROBLEM_21 {
    public static void main(String[] args) {

        Scanner kb=new Scanner(System.in);
        int a;
        System.out.println("Enter range from:");
        a=kb.nextInt();
        int b;
        System.out.println("To");
        b=kb.nextInt();

        int sum=0;

        for(int start=a;a<=b;a++){
            if(a%2==0){
                sum=sum+a;
            }
        }

        System.out.println("The sum of even numbers is "+sum);
    }
}
