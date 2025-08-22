package Sprint_01;

import java.util.Scanner;

public class PROBLEM_19 {
    public static void main(String[] args) {

        Scanner kb=new Scanner(System.in);

        System.out.println("Enter starting number");
        int start=kb.nextInt();

        System.out.println("Enter ending number");
        int end=kb.nextInt();


        for(int a=start;a<=end;a++){

            if(a>1) {
                boolean IsPrime = true;
                for (int i = 2; i < a; i++) {
                    if (a % i == 0) {
                        IsPrime = false;
                        break;
                    }
                }
                if (IsPrime) {
                    System.out.print(a + " ");
                }
            }
        }

    }

//        Once IsPrime is set to false (for a non-prime number), it never resets to true for the next number.














}
