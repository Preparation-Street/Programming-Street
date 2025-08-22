package Sprint_01;
import java.util.Scanner;
class PROBLEM_04{

    public static void main(String[] args) {

        Scanner kb=new Scanner(System.in);
        int num;
        System.out.println("Enter the number");
        num=kb.nextInt();
// Step=01 find length of the number
        int t1=num;
        int length=0;
// Step=02 reverse the number and multiply it
        while(t1!=0){

            t1=t1/10;

            length=length+1;
        }

        int t2=num;
        int rem;
        int arm=0;

        while(t2!=0){
            rem=t2%10;  // Get last digit
            int mul=1;

            for (int i=1;i<=length;i++){

                mul=mul*rem;

            }

            arm=arm+mul;
            t2=t2/10;  // reduce the number

        }
// Check using if else
        if (num==arm){
            System.out.println("It is armstrong no.");
        }
        else{
            System.out.println("It is not a armtrong no.");
        }

    }

}