package Sprint_01;
import java.util.Scanner;

public class PROBLEM_35 {
    public static void main(String[] args) {

        Scanner kb = new Scanner(System.in);
        int range;
        System.out.println("Enter the range: ");
        range=kb.nextInt();

        int sum=0;

        for(int i=2;i<range;i++){
            boolean IsPrime=true;
            for(int j=2;j<i;j++){
                if(i%j==0){
                    IsPrime=false;
                    break;
                }
            }
            if(IsPrime){
                sum=sum+i;
            }
        }

        System.out.println(sum);

    }
}