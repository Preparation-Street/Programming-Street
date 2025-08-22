package Sprint_01;
import java.util.Scanner;

public class PROBLEM_34 {
    public static void main(String[] args) {

        Scanner kb=new Scanner(System.in);
        String st1;
        System.out.println("Enter the first string ");
        st1=kb.next();
        String st2;
        System.out.println("Enter the second string");
        st2=kb.next();

        char []ch1=st1.toCharArray();
        char []ch2=st2.toCharArray();  // Converts both strings into character arrays to make sorting easier.


        for(int i=0;i<st1.length();i++){
            for(int j=i+1;j<st1.length();j++){
                if(ch1[i]>ch1[j]){

                    char temp=ch1[j];
                    ch1[i]=ch1[j];
                    ch1[j]=temp;

                }
            }
        }

        for(int i=0;i<st2.length();i++){
            for(int j=1+1;j<st2.length();j++){
                if(ch2[i]>ch2[j]){

                    char temp=ch2[j];
                    ch2[i]=ch2[j];
                    ch2[j]=temp;

                }
            }
        }

        boolean isAnagram = true;
        for (int i = 0; i < st1.length(); i++) {
            if (ch1[i] != ch2[i]) {
                isAnagram = false;
                break;
            }
        }

        if(isAnagram){
            System.out.println("It is a anagram");
        }
        else{
            System.out.println("It is not a anagram");
        }
    }
}
