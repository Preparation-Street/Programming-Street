package Sprint_01;
import java.util.Scanner;

public class PROBLEM_26 {
    public static void main(String[] args) {

        Scanner kb=new Scanner(System.in);
        int num;
        System.out.println("Enter number: ");
        num=kb.nextInt();

        int temp1=num;
        int length=0;

        while(temp1!=0){
            length=length+1;
            temp1=temp1/10;
        }

        int temp2=num;
        int rem;
        int arm=0;

        while(temp2!=0){
            rem=temp2%10;
            int multi=1;
            for(int i=1;i<=length;i++){
                multi=multi*rem;
            }
            arm=arm+multi;
            temp2=temp2/10;
        }

        if(arm==num){
            System.out.println("It is a narcissistic number "+num);
        }
        else{
            System.out.println("It is not a narcissistic number "+num);
        }
    }
}
