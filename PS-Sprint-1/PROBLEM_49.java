package Sprint_01;

public class PROBLEM_49 {
    public static void main(String[] args) {

        int[]arr={10,20,4,45,99};

        for(int i=0;i<arr.length;i++){
            for(int j=i+1;j<arr.length;j++)

                if(arr[i]<arr[j]){
                int temp=arr[i];
                arr[i]=arr[j];
                arr[j]=temp;

            }

        }

        for(int x:arr){
            System.out.print(x+" ");
        }
        System.out.println("The second largest number in the array is "+arr[1]);
    }
}
