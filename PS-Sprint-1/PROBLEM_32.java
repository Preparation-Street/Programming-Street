package Sprint_01;
public class PROBLEM_32 {
    public static void main(String[] args) {

        int[] arr=new int[]{23,22,45,32,8};
        int n=arr.length;

        for(int i=0;i<arr.length;i++) {
            for (int j = i + 1; j < arr.length; j++) {

                if (arr[i] > arr[j]) {
                    int c = arr[i];
                    arr[i] = arr[j];
                    arr[j] = c;
                }
            }
        }

        int med;

        if(n%2==0){
            med=(arr[n/2-1]+arr[n/2])/2;
        }

        else {
            med = arr[n / 2];
        }

        System.out.println("The median of the sorted array is "+med);
    }
}