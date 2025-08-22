package Sprint_01;

public class PROBLEM_15 {
    public static void main(String[] args) {

       int [] arr=new int[]{3,1,4,1,5,9};

        System.out.print("Original array:");

        for(int i=0;i<arr.length;i++){
            System.out.print(arr[i]+"");
        }

        int temp=0;

        for(int i=0;i<arr.length;i++){
            for(int j=i+1;j<arr.length;j++){
                if(arr[j]<arr[i]){
                    temp=arr[i];
                    arr[i] = arr[j];  // if we don't use temp arr[i] is now arr[j], but we lost the original arr[i] value!
                    arr[j] = arr[i];  // arr[j] is now the same as arr[i], but the original arr[j] is gone!
//                    Without temp, one of the original values would be lost during the assignment.

                }
            }
        }

        System.out.print(" Sorted array is: ");
        for(int i=0;i<arr.length;i++){
            System.out.print(arr[i]+"");
        }
    }
}
