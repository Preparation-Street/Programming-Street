//  Write a program to determine if a number is prime
package Sprint_01;

import java.util.Scanner;

public class PROBLEM_02 {
    public static void main(String[] args) {

        Scanner kb=new Scanner(System.in);
        int a;
        System.out.println("Enter a number to check it is a prime no. or not ");
        a=kb.nextInt();

        boolean isPrime=true;

        if(a<=1){
            isPrime=false;
        }
        else {
            for (int i = 2; i < a; i++) {

                if (a % 2 == 0) {
                    isPrime = false;
                    break;
                }

            }
        }

        if(isPrime){
            System.out.println("It is a prime number");
        }
        else {
            System.out.println("It is not a prime number");
        }


    }
}
