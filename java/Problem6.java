
public class Problem6 {
	public static void main(String[] args) {
		long sum = 0;
		long sosq = 0;
		long diff = 0;
		for (int i=1 ; i<101 ; i++) {
			sum += i;
			sosq += i*i;
		}
		
		diff = sosq - sum*sum;
		System.out.println("diff = " + diff);
	}
}
