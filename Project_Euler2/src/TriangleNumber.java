
public class TriangleNumber {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int tri = 1, numf = 0, numt= 0, arr[] = new int[10];
		//System.out.println("Triangle Number: \n");
	System.out.println(tri + ": \n");
		while(numf < 10) {
			for(int i = 1; i < 10; i++) {
				for(int j = 0; j < i; j++) {
				tri *=i;
				//arr[i] = tri;
				System.out.println("Triangle Number: " + tri);
				System.out.println(tri +  " \n");
				numf++;
				}
			}
		}
	}

}
