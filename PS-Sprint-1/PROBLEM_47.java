package Sprint_01;

import java.util.Scanner;

public class PROBLEM_47 {
    public static void main(String[] args) {

        Scanner kb=new Scanner(System.in);
        int rows;
        System.out.println("Enter no. of rows ");
        rows=kb.nextInt();

        for(int i=1;i<=rows;i++){
            for(int j=1;j<i+1;j++){
                System.out.print(j);
            }
            System.out.println();
        }

    }
}
