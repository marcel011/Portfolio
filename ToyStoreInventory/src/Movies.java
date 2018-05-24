import java.util.*;
import java.lang.*;
public class Movies extends Product  { 
	private long upc;
	
	private ArrayList<Movies> mv = new ArrayList<Movies>();
	public Movies(long upc, long sku, String title,
			double price, int qty){
		super(sku, title, price, qty);
		setUPC(upc);
	//	this.upc = upc; 
	}
	/*public void addProduct(Movies m) {
		mv.add(m);
	}
	public void removeProduct(Movies m) {
		mv.remove(m);
	}*/
	public String displayProduct() {
		return super.displayProduct() + "upc="+upc + "\n";
	}
	public String displaySort() {
		return "Movie\t" + super.displaySort();
	}
	public void setUPC(long u) {
		upc = u;
	}
	public int compare(Product pr, Product qr) {
		 long lhp = pr.getSKU();
		    long rhp = qr.getSKU();
		   
		    if (lhp < rhp)
		 return -1;
		    
		    if (lhp == rhp )
		    	return 0;
		    
		    return 1;
		   
		}
public void processSale(int qt, double co) {
	 double totprice = 0, profit = 0, totcred=0, totcomm=0, totshcred=0, shcred=0;
	  totprice = getPrice()*getQuantity();
	  System.out.println("Price: " + getPrice() + "\tQuantity: " + getQuantity() + "\n");
	  shcred = 2.98*getQuantity();
	  totshcred = shcred*getQuantity();
	  totcomm = (.12*getQuantity());
	  profit =  totprice + totshcred - (totcomm+co);
	  System.out.println("Total Price: $" + totprice + "\n" + "Total Shipping Credit: $" +
	  + totshcred +  "\n" + "Total Commision: $" + totcomm + "\n" + 
		"Profit: $" + profit + "\t");
}
	
}
