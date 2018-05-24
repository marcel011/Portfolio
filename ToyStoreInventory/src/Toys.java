import java.util.*;
import java.lang.*;
public class Toys extends Product {
	private double weight; 
	
	private ArrayList<Toys> ty = new ArrayList<Toys>();
	public Toys(long sku, String title,
			double price, int qty, double weight){ 
		super(sku, title, price, qty);
		this.weight = weight;
}
	/*public void addProduct(Toys t) {
		ty.add(t);
	}
	public void removeProduct(Toys t) {
		ty.remove(t);
	}*/
	public String displayProduct() {
		return super.displayProduct() + weight + "\n";
	}
	public String displaySort() {
		return "Toy\t" + super.displaySort();
	}
public void displayTable() {
		for(Toys t : ty) {
			System.out.println(t);
		}
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
		 int lb= (int) (weight/16);
		  totprice = getPrice()*getQuantity();
		  System.out.println("Price: " + getPrice() + "\tQuantity: " + getQuantity() + "\n");
		  shcred = (4.49*(.5*lb))*getQuantity();
		  totshcred = shcred*getQuantity();
		  totcomm = (.15*getQuantity());
		  profit =  totprice + totshcred - (totcomm+co);
		  System.out.println("Total Price: $" + totprice + "\n" + "Total Shipping Credit: $" +
		  + totshcred +  "\n" + "Total Commision: $" + totcomm + "\n"
		   + "Profit: $" + profit + "\n");
	}
	
	
}
