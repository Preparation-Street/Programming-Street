package Sprint_01;
import java.util.Scanner;

public class PROBLEM_37 {
    public static void main(String[] args) {

        Scanner kb=new Scanner(System.in);
        int num;
        System.out.println("Enter the number");
        num=kb.nextInt();

        boolean isPerfect=false;

        for(int i=1;i<num;i++){
            double sq=Math.pow(i,2);

            if(sq==num){
                isPerfect=true;
                break;
            }

        }

       if(isPerfect){
           System.out.println("It is a perfect square");
       }

       else{
           System.out.println("It is not a perfect square");
       }
    }
}
