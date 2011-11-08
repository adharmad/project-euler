
public class Problem2 {
	public static void main(String[] args) {
		long sum = 0;
		int i = 1;
		long f = 0;
		
		while ((f = fib(i)) < 4000000) {
			sum += (f%2==0? f : 0);
			i++;
		}
		
		System.out.println("sum = " + sum);
		
	}
	
	public static long fib(int i) {
		if (i == 1) return 0;
		else if (i == 2) return 1;
		else return fib(i-1) + fib(i-2);
	}
}
