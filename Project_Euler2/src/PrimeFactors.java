import java.util.*;

public class PrimeFactors {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		
		
		int i, j, max = 2, prime = 2; 
		//num = 13195;
		
		long num = 600851475143L;
		for(i= 2; i < Math.sqrt(num); i++) {
			
			for(j = 2; j <= i; j++) {
				if(i==j) {
					prime = i;
					//System.out.println(prime);
						 }
									
				if(i%j == 0)
					break;
									}
			if(num % prime == 0) 
				max = prime;
								}
		
			
			
		System.out.println(max);
		
	}

}
