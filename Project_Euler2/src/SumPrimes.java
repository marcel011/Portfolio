import java.io.*;
import java.util.*;
import java.lang.*;

public class SumPrimes {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//int i = 2, j, prime = 2, cnt = 0, pos = 0, sum = 0;
		int n = 2000000;
		boolean notPrimes[] = new boolean[n];   // default = false
	    for ( int i = 2 ; i*i < n ; i++ ) {
	        if ( !notPrimes[i] ) {
	            for ( int j = i*i ; j < n ; j+=i ){
	                notPrimes[j] = true;
	            }
	        }
	    }
	    long sum = 2 ;
	    for ( int i = 3 ; i < n ; i+=2 ) {
	        if ( !notPrimes[i] ) {
	            sum+=i;
	        }
	    }
	    System.out.println(sum);
	
	}
}
