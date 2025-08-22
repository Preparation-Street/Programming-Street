package Sprint_01;

import java.util.Scanner;

class PROBLEM_05{
    public static void main(String[] args) {

        Scanner kb=new Scanner(System.in);
        int limit;
        System.out.println("Enter limit");
        limit=kb.nextInt();

        int a=0;
        System.out.print(a+"");
        int b=1;
        if(limit>=1){
            System.out.print(b+"");
        }

        for(;;){
            int c=a+b;
            if(c>limit){
                break;
            }
            System.out.print(c);
            a=b;
            b=c;
        }











    }
}