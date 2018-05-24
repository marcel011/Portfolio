import java.io.*;
import java.lang.*;
import java.util.*;

public class SumSquareDiff {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int sumsq = 0, squaresm = 0, diff = 0,i, j, sum = 0;
		
		for(i=1; i <= 100; i++) {
			sumsq += i*i;
			sum +=i;
		}
		squaresm = sum*sum; 
		diff = squaresm - sumsq;
		System.out.println("Sum of squares: " + sumsq + "\nSquare of sums:  " 
	+ squaresm + "\n Difference: " + diff); 
	}

}
