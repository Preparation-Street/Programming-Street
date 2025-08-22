package Sprint_01;

import java.util.Scanner;

public class PROBLEM_18 {
    public static void main(String[] args) {

        Scanner kb=new Scanner(System.in);
        int a;
        System.out.println("Enter number");
        a=kb.nextInt();
        int b;
        System.out.println("Upto ?");
        b=kb.nextInt();

        int multi=0;

        for(int i=1;i<=b;i++){

            multi=a*i;
            System.out.println(a+"*"+i+" = "+multi);

        }
    }
}
