package Sprint_01;

import java.util.Scanner;

public class PROBLEM_20 {
    public static void main(String[] args) {

        Scanner kb=new Scanner(System.in);
        int num;
        System.out.println("Enter number");
        num=kb.nextInt();

        int sum=0;

        for(int i=1;i<num;i++){
            if(num%i==0){
                sum=sum+i;
            }
        }

        if(num==sum){
            System.out.println("It is a perfect square");
        }

        else {
            System.out.println("It is not a perfect square");
        }
    }
}
