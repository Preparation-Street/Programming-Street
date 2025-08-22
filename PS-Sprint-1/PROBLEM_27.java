package Sprint_01;

import java.util.Scanner;

public class PROBLEM_27 {

    public static void main(String[] args) {

        Scanner kb=new Scanner(System.in);
        int num;
        System.out.println("Enter number ");
        num=kb.nextInt();

        for(int i=1;i<=num;i++){
            for(int j=i; j<2*i;j++){
                System.out.print(j);
            }
            System.out.println();

        }
    }
}
