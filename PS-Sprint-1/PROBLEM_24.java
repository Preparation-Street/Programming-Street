package Sprint_01;
import java.util.Scanner;

class PROBLEM_24{
    public static void main(String[] args) {

        Scanner kb=new Scanner(System.in);
        int num;
        System.out.println("Enter number");
        num=kb.nextInt();

        for(int i=2;i<num;i++){
            boolean IsPrime=true;

            for(int j=2;j<i;j++){
                if (i % j == 0) {
                    IsPrime=false;
                    break;
                }
            }

            if(IsPrime) {
                System.out.print(i+" ");
            }
        }
    }
}

