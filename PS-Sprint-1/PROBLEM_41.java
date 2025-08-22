package Sprint_01;
import java.util.Scanner;

public class PROBLEM_41 {
    public static void main(String[]args){

        Scanner kb=new Scanner(System.in);
        int num;
        System.out.println("Enter the number");
        num=kb.nextInt();
        int digit;
        System.out.println("Enter the digit ");
        digit=kb.nextInt();

        int length=0;
        int temp=num;

        while(temp!=0){
            length++;
            temp=temp/10;
        }

        int occur=0;
        int temp1=num;
        for(int i=1;i<length;i++){

            int temp2=temp1%10;

            if(temp2==digit){
                occur++;
            }

            temp1=temp1/10;
        }
        System.out.println("The digit "+digit+" occurs "+occur+" times in the number "+num);
    }
}
