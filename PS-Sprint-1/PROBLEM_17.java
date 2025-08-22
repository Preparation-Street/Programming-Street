package Sprint_01;

import java.util.Scanner;

class PROBLEM_17{
    public static void main(String[] args) {

        Scanner kb=new Scanner(System.in);
        int start;
        System.out.println("Enter starting number");
        start=kb.nextInt();

        int end;
        System.out.println("Enter ending number");
        end=kb.nextInt();

       for(int a=start;a<=end;a++){
        int t1=a;
           int length=0;
           while (t1!=0){
               t1=t1/10;
               length=length+1;
           }

           int t2=a;
           int rem;
           int arm=0;

           while(t2!=0) {

               rem = t2 % 10;
               int multi = 1;

               for (int i = 0; i < length; i++) {
                   multi = multi * rem;
               }

               arm = arm + multi;
               t2 = t2 / 10;
           }
           if(a==arm){
               System.out.print(arm+" ");
           }
       }
    }
}

