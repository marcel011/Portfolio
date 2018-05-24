
public class PythagoreanTriplets {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int a = 0, b=0, c=0, trip = 0, a2 = 0, b2 = 0, c2 = 0;
		for(a = 1; a < 1000; a++) {
			for(b = 2; b < 1000; b++) {
				for(c= 3; c < 1000; c++) {
		if((a < b) && (b < c) && ((a+b+c) == 1000)) {
			if((a*a) + (b*b) == (c*c)) {
				a2 = a;
			    b2 = b;
			    c2 = c;
			}
		}
		}
		}
		}
		System.out.println(a2+"*"+b2+"*"+c2 +" = " +(a2*b2*c2));
	}

}
