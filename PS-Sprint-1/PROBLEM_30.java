package Sprint_01;

public class PROBLEM_30 {
    public static void main(String[] args) {

        int[] arr=new int[]{1,2,4,5};
        int sum=0;
        int arrsum=0;

        int n=arr.length+1;

        sum=n*(n+1)/2;

        for (int j=0;j<arr.length;j++){
            arrsum=arrsum+arr[j];
        }


        int missnum=sum-arrsum;

        System.out.println("Missisng number is "+missnum);
    }
}
