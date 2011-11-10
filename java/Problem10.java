
public class Problem10 {
	public static void main(String[] args) {
		long sum = 0;
		
		for (int i=1 ; i<2000000 ; i++) {
			sum += (is_prime(i)? i : 0);
		}
		
		System.out.println(sum);
	}
	
	public static boolean is_prime(int num) {
		if (num == 1) return false;
		if (num == 2) return true;
		if (num == 3) return true;
		
		for (int i=2 ; i<=Math.sqrt(num) ; i++) {
			if (num%i == 0) return false;
		}
			
		return true;
	}		
}
