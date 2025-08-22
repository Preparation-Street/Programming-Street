package Sprint_01;
import java.util.Scanner;

public class PROBLEM_43 {
    public static void main(String[] args) {

        Scanner kb=new Scanner(System.in);
        int num;
        System.out.println("Enter the number ");
        num=kb.nextInt();

        for(int i=1;i<=num;i++){
            if(num%i==0){
                System.out.print(i+" ");
            }
        }
    }
}
