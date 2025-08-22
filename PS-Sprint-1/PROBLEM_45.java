package Sprint_01;

public class PROBLEM_45 {
    public static void main(String[] args) {

     int[] arr ={1,2,2,3,4,4,4};
     int maxcount=0;
     int mode=arr[0];

     for(int i=0;i<arr.length;i++){
         int count =0;

         for(int j=0;j<arr.length;j++){

             if(arr[i]==arr[j]){
                 count++;

             }
             if(count>maxcount){

                 maxcount=count;
                 mode=arr[i];

             }
         }
     }
        System.out.println("Mode of the given array is "+mode);
    }
}
