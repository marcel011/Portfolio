
public class NthPrime {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int i = 2, j, prime = 2, cnt = 0, pos = 0;
		boolean flag = false;
		
		while(pos < 10002) {
			
			cnt = 0;
			flag = false;
			for(j = 2; j <= i; j++) {
				
				if(i==j) {
				prime = i;
				flag = true;
				cnt++;
					 }
				if(flag) {
					pos++;
				}
				if(cnt == 1 && pos == 10001) {
					System.out.println(pos + "th prime is: " + prime);
					
				}
			if(i%j == 0)
				break;
			
		
								}
			i++;
		}
	}

}
