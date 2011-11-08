
public class Problem7 {
	public static void main(String[] args) {
		int i = 0;
		int num = 2;
		
		while (true) {
			if (is_prime(num)) i++;
			num++;
			
			if (i == 10001) break;
		}
		
		System.out.println("10001th prime = " + num);
	}
	
	public static boolean is_prime(int num) {
		if (num == 2) return true;
		
		for (int i=2 ; i<Math.sqrt(num) ; i++) {
			if (num%i == 0) return false;
		}
			
		return true;
	}	
}
