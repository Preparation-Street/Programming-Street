package Sprint_01;

public class PROBLEM_50 {
    public static void main(String[] args) {

        String sr="abcdefabcd";
        String longest="";

        for(int i=0;i<sr.length();i++){
            String current="";
            for(int j=i;j<sr.length();j++){

                char ch=sr.charAt(j);

                if(current.indexOf(ch)!=-1){
                    break;
                }

                current=current+ch;
                if(current.length()>longest.length()){
                    longest=current;
                }
            }
        }

        System.out.println("Longest substring is "+longest);
    }
}
