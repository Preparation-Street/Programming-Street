import java.util.Scanner;

public class ps6_palindrome {

    public static int reverse(int num){
        int revNum =0;

        while (num>0) {
            int rem = num%10;
            revNum = revNum*10 + rem;

            num /= 10;
        }

        return revNum;
    }

    public static void palindrome(int n){
        int n1 = n;

        if(reverse(n) == n1){
            System.out.println("Palindrome");
        } else{
            System.out.println("Not Palindrome");
        }
       
    }
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a num : ");
        int num = sc.nextInt();

        palindrome(num);

        sc.close();


    }
}