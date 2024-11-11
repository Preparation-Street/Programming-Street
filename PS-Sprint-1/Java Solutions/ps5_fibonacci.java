import java.util.Scanner;

public class ps5_fibonacci {

    public static void fibonacci(int lim){
        int fib1 = 0, fib2 = 1;

        System.out.print(fib1 + " " + fib2 + " ");
        while(lim - 2 > 0){
            int fib3 = fib1 + fib2;
            System.out.print(fib3 + " ");
            fib1 = fib2;
            fib2 = fib3;
            
            lim--;
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter fibonacci limit : ");
        int limit = sc.nextInt();

        fibonacci(limit);
        sc.close();

    }
}
