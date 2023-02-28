public class TribonacciNumber{
    public int tribonacciNumber(int n){
        int x=0,y = 1,z=1;
        if (n==0) return x;
        if (n==1) return y;
        if (n==2) return z;
        for (int i=0; i<=n-3; i++){
            int sums = x+y+z;
            x = y;
            y = z;
            z = sums;
        }
        return z;
    }
}