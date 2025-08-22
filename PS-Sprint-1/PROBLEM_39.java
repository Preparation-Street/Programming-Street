package Sprint_01;

import java.util.Scanner;

public class PROBLEM_39 {

    public static void main(String[] args) {

        Scanner kb=new Scanner(System.in);
        int rows;
        System.out.println("Enter no. of rows ");
        rows=kb.nextInt();

        int count=1;

        for(int i=0;i<rows;i++){
            for(int j=0;j<rows;j++){
                System.out.print(count+" ");
                count++;
            }
            System.out.println();
        }
    }
}
