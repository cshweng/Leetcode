public class Q392_is_Subsequence{
    public boolean isSubsequence(String s, String t){
        if (s.length()==0){
            return true;
        }
        int len = t.length();
        for (int i=0;i<len;i++){
            if(s.charAt(0)==t.charAt(0)){
                s=s.substring(1);
            }
            t=t.substring(1);
            if (s.length()==0){
                return true;
            }
        }
        return false;
    }
}