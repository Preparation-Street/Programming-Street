package Sprint_01;

import java.util.Scanner;

public class PROBLEM_13 {
    public static void main(String[] args) {

        Scanner kb=new Scanner(System.in);
        String sr;
        System.out.println("Enter String");
        sr=kb.nextLine();

        String rev="";

        for(int i = sr.length()-1; i >= 0; i--){
            char ch=sr.charAt(i);
            rev=rev+ch;

        }
        System.out.println("Reverse of a string is: "+rev);
    }
}
