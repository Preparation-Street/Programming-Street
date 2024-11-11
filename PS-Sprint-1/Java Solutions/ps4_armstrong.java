import java.util.*;

public class ps4_armstrong {

    public static void amstrongNum(int num){
        int isNum = num;
        // int digit = 0;
        int digit = String.valueOf(num).length();

        // int dNum= num;
        // while(dNum > 0){
        //     dNum /= 10;
        //     digit++;
        // }

        int finalNum = 0;
        while(num > 0){
            int rem = num %10;
            finalNum = finalNum + (int)Math.pow(rem, digit);

            num /= 10;
        }
        if(isNum == finalNum){

            System.out.println(finalNum + " is an Amstrong number" );
        } else{
            System.out.println(isNum + " Not an Amstrong number");
        }
    }
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a num : ");
        int num = sc.nextInt();

        amstrongNum(num);
        sc.close();

    }
}
