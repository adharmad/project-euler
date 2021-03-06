
public class Problem7 {
	public static void main(String[] args) {
		int i = 0;
		int num = 0;
		
		while (true) {
			num++;
			if (is_prime(num)) i++;
			
			
			if (i == 10001) break;
		}
		
		System.out.println("10001th prime = " + num);
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
