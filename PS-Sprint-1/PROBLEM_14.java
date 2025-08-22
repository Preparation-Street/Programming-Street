package Sprint_01;

public class PROBLEM_14 {
    public static void main(String[] args) {

        int[] arr =new int[]{22,34,21,12,34};

        int smallest=arr[0];
        int largest=arr[0];

        for(int i=1;i<arr.length;i++){
            if(arr[i]>largest){
                largest=arr[i];
            }
            else if (arr[i]<smallest){
                smallest=arr[i];
            }
        }
        System.out.println("Largest is "+largest+" Smallest is: "+smallest);
    }
}
