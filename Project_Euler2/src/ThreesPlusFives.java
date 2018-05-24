import java.io.*;
import java.lang.*;
import java.util.*;

public class ThreesPlusFives {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
    	System.out.println("This program counts the sum of integers divisible "
    		+"by 3 & 5. "	+ "Enter number: ");
    	
    	int num = sc.nextInt();
    	System.out.println("Your number: "+ num);
    int sum = 0, i;
    for(i = 1; i < num; i++) {
    	if(i % 5 == 0)
    		sum+= i;
    	else if(i % 3 == 0)
    		sum+=i;
    }
    System.out.println("The sum of integers divisible by 3 or 5 under "
    		+ num + " is: " + sum);
    
	}

}
