package Sprint_01;

import java.util.Scanner;

class PROBLEM_12{
    public static void main(String[] args) {

        Scanner kb=new Scanner(System.in);
        String sr;
        System.out.println("Enter String");
        sr=kb.next();

        String srt=sr.toLowerCase();
        int vowel=0;
        int consonant=0;

        for(int i=0;i<srt.length();i++){
            char ch=srt.charAt(i);

            if(ch=='a'|| ch=='e'||ch=='i'||ch=='o'||ch=='u'){
                vowel++;
            }
            else if(ch>='a'&&ch<='z'){
                consonant++;
            }
        }

        System.out.println("Vowels are "+vowel+" Consonants are "+consonant);







    }
}