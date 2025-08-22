package Sprint_01;

import java.util.Scanner;

public class PROBLEM_31 {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        System.out.print("How many rows? ");
        int n = sc.nextInt();

        int[][] triangle = new int[n][n];

        for (int row = 0; row < n; row++) {
            for (int col = 0; col <= row; col++) {
                // First or last element is always 1
                if (col == 0 || col == row) {
                    triangle[row][col] = 1;
                } else {
                    // Middle elements = sum of two numbers from above
                    triangle[row][col] = triangle[row - 1][col - 1] + triangle[row - 1][col];
                }

                System.out.print(triangle[row][col] + " ");
            }
            System.out.println();
        }
    }
}
