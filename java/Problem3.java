
public class Problem3 {
	public static void main(String[] args) {
		long num = 600851475143L;
		long largest_prime_factor = 0;
		
		for (int i=2 ; i<Math.sqrt(num) ; i++) {
			largest_prime_factor = (is_prime(i) && num%i == 0 ? i : largest_prime_factor); 
		}
		
		System.out.println("largest prime factor = " + largest_prime_factor);
	}
	
	public static boolean is_prime(int num) {
		if (num == 2) return true;
		
		for (int i=2 ; i<Math.sqrt(num) ; i++) {
			if (num%i == 0) return false;
		}
			
		return true;
	}
}
