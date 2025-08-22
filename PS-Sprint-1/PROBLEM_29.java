package Sprint_01;

import java.util.Scanner;

public class PROBLEM_29 {
    public static void main(String[] args) {

        Scanner kb=new Scanner(System.in);
        System.out.println("Enter string");
        String st;
        st=kb.nextLine();

        String rev="";
        int left=0;
        int right=st.length()-1;

        while(left<right){
            if(st.charAt(left)!=st.charAt(right)){

                left++;
                right--;
            }
            else {
                rev=rev+st.charAt(right);
            }

            System.out.println(rev);

        }
    }
}
