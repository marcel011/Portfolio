import java.util.*;
import java.lang.*;
public class Palindrome {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int conc, num = 1000, max, i, j, l;
		boolean flag = false;
		String palindrome, cand, max_p;
		Palindrome p;
		
		conc = 1001;
		max = conc;
		System.out.println("Conc: "+ conc);
		palindrome = Integer.toString(max);
		
		/*if(isPalindrome(palindrome))
		System.out.println("Biggest prime: " + palindrome);*/
		for(i = 100; i < num; i++) {
			for(j = 100; j < num; j++) {
				conc = i*j;
				
				cand = Integer.toString(conc);
				
					System.out.println("Cand: " + cand);
					
														   if(isPalindrome(cand) && Integer.parseInt(cand) > Integer.parseInt(palindrome)){
															   palindrome = cand;
														   System.out.println("Current Biggest Palindrome: " + palindrome);
								   									}
									 }
								 }
		System.out.println("Biggest Palindrome: " + palindrome);
		
		
	}
	public static boolean isPalindrome(String cand) {
		int k,l;
		 l = cand.length() - 1;
		boolean flag = false;
		System.out.println("Cand: " + cand);
		for(k = 0; k <= ((cand.length() - 1)/2); k++) {
			System.out.println("Charcacter " + "k: "+ cand.charAt(k));
			

			
				System.out.println("Charcacter " + "l: "+ cand.charAt(l));
				if(l==k) {
					flag = true;
					break;
				}
				if(cand.charAt(k) == cand.charAt(l))
					flag = true;
				else {
					flag = false;
					break;
				}
				l--;
		}
		System.out.println("Flag: " + flag);
		return flag;
											   }
	
											   
	
}




