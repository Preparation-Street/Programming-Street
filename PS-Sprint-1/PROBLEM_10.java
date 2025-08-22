package Sprint_01;

import java.util.Scanner;

class PROBLEM_10{
    public static void main(String[] args) {

        Scanner kb=new Scanner(System.in);
        int a,b;
        System.out.println("Enter two number");
        a=kb.nextInt();
        b=kb.nextInt();

        int min = Math.min(a, b);

        for (int i=min;i>=1;i--){
            if (a%i==0 && b%i==0){
                System.out.println("GCD is "+i);
                break;
            }
        }












    }
}