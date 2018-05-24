import java.io.*;
import java.util.*;
import java.lang.*;
public class LargestProductSeries {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
int one = 0, two = 0, three = 0, four = 0, five=0, six = 0, seven=0,
eight = 0, nine=0, ten = 0, eleven = 0, twelve = 0, thirteen = 0,big = 0, i, sub = 0,
oneb = 0, twob = 0, threeb=0, fourb = 0, fiveb = 0, sixb = 0, sevenb = 0, eightb = 0,
nineb = 0, tenb = 0, elevenb = 0, twelveb = 0, thirteenb = 0;
String num = "73167176531330624919225119674426574742355349194934" +
"96983520312774506326239578318016984801869478851843" +
"85861560789112949495459501737958331952853208805511" +
"12540698747158523863050715693290963295227443043557" +
"66896648950445244523161731856403098711121722383113" +
"62229893423380308135336276614282806444486645238749" +
"30358907296290491560440772390713810515859307960866" +
"70172427121883998797908792274921901699720888093776" +
"65727333001053367881220235421809751254540594752243" +
"52584907711670556013604839586446706324415722155397" +
"53697817977846174064955149290862569321978468622482" +
"83972241375657056057490261407972968652414535100474" +
"82166370484403199890008895243450658541227588666881" +
"16427171479924442928230863465674813919123162824586" +
"17866458359124566529476545682848912883142607690042" +
"24219022671055626321111109370544217506941658960408" +
"07198403850962455444362981230987879927244284909188" +
"84580156166097919133875499200524063689912560717606" +
"05886116467109405077541002256983155200055935729725" +
"71636269561882670428252483600823257530420752963450";

//String seq = Long.toString(num);
char carr[] = num.toCharArray();
System.out.println(num);
for(int j = 0; j < 5; j++) {
	System.out.println(num.charAt(j));
}
for(i = 0; i < carr.length - 14; i++) {
	one = Character.getNumericValue(carr[i]);
	
	System.out.println(one);
	two = Character.getNumericValue(carr[i + 1]);
	
	three = Character.getNumericValue(carr[i+ 2]);
	
	four = Character.getNumericValue(carr[i + 3]);
	
	five = Character.getNumericValue(carr[i + 4]);
	six = Character.getNumericValue(carr[i + 5]);
	seven = Character.getNumericValue(carr[i + 6]);
	eight = Character.getNumericValue(carr[i + 7]);
	nine = Character.getNumericValue(carr[i + 8]);
	ten = Character.getNumericValue(carr[i + 9]);
	eleven = Character.getNumericValue(carr[i + 10]);
	twelve = Character.getNumericValue(carr[i + 11]);
	thirteen = Character.getNumericValue(carr[i + 12]);
	sub = one*two*three*four*five*six*seven*eight*nine*ten*eleven*twelve*thirteen;
	System.out.println("Biggest Substring is: " + one + "*" +
	two + "*" + three +  "*" + four + "*" + five + "*" + six + "*" + seven +
	"*"+ eight + "*" + nine + "*" + ten + "*" + eleven + "*" + twelve + "*"
	+ thirteen + " = " + sub);
	
	if(sub > big) {
		big = sub;
		oneb = one;
		twob = two;
		threeb = three;
		fourb = four;
		fiveb = five;
		sixb = six;
		sevenb = seven;
		eightb = eight;
		nineb = nine;
		tenb = ten;
		elevenb = eleven;
		twelveb = twelve;
		thirteenb = thirteen;
	}
	
}
System.out.println("Biggest Substring is: " + oneb + "*" +
		twob + "*" + threeb +  "*" + fourb + "*" + fiveb + "*" + sixb + "*" + sevenb +
		"*"+ eightb + "*" + nineb + "*" + tenb + "*" + elevenb + "*" + twelveb + "*"
		+ thirteenb + " = " + big);

	}

}
