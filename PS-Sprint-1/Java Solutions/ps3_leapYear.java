import java.util.Scanner;

public class ps3_leapYear {

    public static void leapYr(int year){
        if(year%4==0 && (year%100 != 0 || year%400 == 0)){
            System.out.println(year + " is a Leap Year");
        } else{
            System.out.println(year + " is not Leap Year");
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a year : ");
        int yr = sc.nextInt();

        leapYr(yr);
        sc.close();

    }
}