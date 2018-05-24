import java.util.*;
import java.lang.*;
import java.io.*;
public class SmallMultiple {

	public static void main(String[] args) {
		int mult = 0, i = 1, num = 0;
		boolean flag = true;
		while(flag) {
			System.out.println("Before Loop: " + num);
			for(i = 20; i > 0; i--) {
				System.out.println("i: " + i + ", " + num+ " % i: " + num%i);
			if(num%i != 0)
				break;
			if(i == 6 && ((num%i) == 0) && num != 0) {
				mult = num;
				flag =false;
				break;
			}
			}
			if(flag)
			num+=380;
		}

		System.out.println("After Loop: " + num);
					
	}
	}

