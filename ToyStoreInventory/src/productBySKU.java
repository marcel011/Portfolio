import java.util.*;
public class productBySKU implements Comparator<Product> {
public int compare(Product pr, Product qr) {
	 long lhp = pr.getSKU();
	    long rhp = qr.getSKU();
	   
	    if (lhp < rhp)
	 return -1;
	    
	    if (lhp == rhp )
	    	return 0;
	    
	    return 1;
	   
	}
}
