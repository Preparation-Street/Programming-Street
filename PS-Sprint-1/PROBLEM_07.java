package Sprint_01;
import java.util.Scanner;

public class PROBLEM_07 {
    public static void main(String[] args) {

        Scanner kb=new Scanner(System.in);
        int num;
        System.out.println("Enter rows no.");
        num=kb.nextInt();

        for(int i=1;i<=num;i++){
            for(int space=num-i;space>=1;space--){
                System.out.print(" ");
            }
            for(int j=1;j<=(2*i-1);j++){
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
