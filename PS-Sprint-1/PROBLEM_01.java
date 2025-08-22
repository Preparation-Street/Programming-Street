//  Write a program to check whether a number is even or odd.

package Sprint_01;

import java.util.Scanner;

public class PROBLEM_01 {
    public static void main(String[] args) {

        Scanner kb=new Scanner(System.in);
        int a;
        System.out.println("Enter the number");
        a=kb.nextInt();

        if(a==0){
            System.out.println("Zero is neither even nor odd");
        }
        else if (a%2==0) {
            System.out.println("It is a even no.");

        }
        else {
            System.out.println("It is a odd no.");
        }

    }





}
