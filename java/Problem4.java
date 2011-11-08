
public class Problem4 {
	public static void main(String[] args) {
		int prod = 0;
		int largest_palindrome = 0;
		
		for (int i=100 ; i<1000 ; i++){
			for (int j=100 ; j<1000 ; j++){
				prod = i*j;
				if (is_palindrome(prod) && prod > largest_palindrome) {
					largest_palindrome = prod;
				}
			}
		}
		
		System.out.println("largest palindrome = " + largest_palindrome);
	}
	
	public static boolean is_palindrome(int num) {
		String s = num+"";
		
		int i=0, j=s.length()-1;
		while (i <= j) {
			if (s.charAt(i++) != s.charAt(j--)) {
				return false;
			}
		}
		
		return true;
	}
}
