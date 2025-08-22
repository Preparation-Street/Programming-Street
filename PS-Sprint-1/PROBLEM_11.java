package Sprint_01;

import java.util.Scanner;

public class PROBLEM_11 {
    public static void main(String[] args) {

        Scanner kb=new Scanner(System.in);
        System.out.println("Enter the number a");
        int a=kb.nextInt();
        System.out.println("Enter the number b");
        int b=kb.nextInt();

    int max=Math.max(a,b);

    while(true) {

        if (max % a == 0 && max % b == 0) {

            System.out.println("LCM is " + max);
            break;

        }

        max++;
    }

    }

    }














