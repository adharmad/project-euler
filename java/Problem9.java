
public class Problem9 {
	public static void main(String[] args) {
		for (int a=1 ; a<998 ; a++) {
			for (int b=1 ; b<998 ; b++) {
				for (int c=1 ; c<998 ; c++) {
					if (is_pythagorean_triplet(a, b, c) && (a+b+c == 1000)) {
						System.out.println(a*b*c);
					}
				}
			}
		}
	}
	
	public static boolean is_pythagorean_triplet(int a, int b, int c) {
		return (a*a + b*b == c*c);
	}
}
