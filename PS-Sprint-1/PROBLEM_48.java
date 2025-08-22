package Sprint_01;

import java.util.Scanner;

public class PROBLEM_48 {
    public static void main(String[] args) {

        Scanner kb=new Scanner(System.in);
        int num;
        System.out.println("Enter the number");
        num=kb.nextInt();

        int sum=0;

        for(int i=2;i<=num;i++){
            if(num%i==0){
                sum=sum+i;  // Add the unique prime factor

            while(num%i==0){
                num=num/i;  // Keep dividing by i to remove all occurrences
            }

            }
        }

        System.out.println("Their sum is "+sum);
    }
}
