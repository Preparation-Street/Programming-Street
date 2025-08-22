package Sprint_01;

public class PROBLEM_44 {
    public static void main(String[]args){

        int[]arr=new int[]{1,2,3,4};

        int sum=0;

        for(int i=0;i<arr.length;i++){
            sum=sum+arr[i];
        }

        double avg=(double)sum/ arr.length;

        System.out.println("The average of the given array is "+avg);
    }
}
