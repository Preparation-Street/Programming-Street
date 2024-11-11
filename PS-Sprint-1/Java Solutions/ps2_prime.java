import java.util.Scanner;

public class ps2_prime {

    public static boolean isPrime(int num){
        if(num == 2) return true;

        for (int i = 3; i < Math.sqrt(num); i++) {
            if(num%i==0){
                return false;
            }
        }

        return true;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a num : ");
        int num = sc.nextInt();

        if(isPrime(num)){
            System.out.println("The number is a prime number.");
        } else { 
            System.out.println("The number is not a prime number.");
        }

        sc.close();
    }   
}
