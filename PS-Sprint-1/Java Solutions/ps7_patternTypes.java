import java.util.Scanner;

public class ps7_patternTypes {

    public static void simplePyramid(int x){
        for (int i = 0; i < x; i++) {
            for (int j = 0; j <x-i-1 ; j++) {
                System.out.print(" ");
            }

            for (int j = 0; j < 2*i+1; j++) {
                System.out.print("*");
            }

            System.out.print("\n");
        }
    }

    public static void invertPyramid(int x){
        for (int i = 0; i < x; i++) {
            for (int j = 0; j < i; j++) {
                System.out.print(" ");
            }

            for(int j = 0; j<2*x-2*i-1; j++){
                System.out.print("*");
            }

            System.out.println("");
        }
    }

   
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Choose one --\n1. Simple Pyramid\n2. Inverted Pyramid");
        int n = sc.nextInt();
        System.out.println("Enter row num : ");
        int rowNum = sc.nextInt();
        System.out.println("Your pattern is below : \n");
        switch (n) {
            case 1:
            simplePyramid(rowNum);
                break;

            case 2:
            invertPyramid(rowNum);
                break;
        
            default: 
            System.out.println("Option Invalid.");
                break;
        }
        
    }
}
