package Sprint_01;
import java.util.Scanner;

public class PROBLEM_42 {
    public static void main(String[]args){

        Scanner kb=new Scanner(System.in);
        int n;
        System.out.println("Enter the number");
        n=kb.nextInt();

        for(int i=0;i<n;i++){
            System.out.print(fibbonacci(i)+" ");
        }

    }

    private static long fibbonacci(int n) {
        if(n==0) return 0;
        if(n==1) return 1;
        return fibbonacci(n-1)+fibbonacci(n-2);
    }
}
