package Sprint_01;
import java.util.Scanner;

public class PROBLEM_23 {
    public static void main(String[] args) {

        Scanner kb=new Scanner(System.in);
        int position;
        System.out.println("Enter position");
        position=kb.nextInt();

        int a=0;
        int b=1;
        System.out.print(a+" "+b+" ");

        for(int i=1;i<=position;i++){
            int c=a+b;
            a=b;
            b=c;
            System.out.print(c+" ");
            if(c==position){
                break;
            }
        }
    }
}
