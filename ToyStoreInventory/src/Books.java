import java.util.*;
import java.lang.*;
public class Books extends Product {
	private long isbn;
	private String title, author;
	 
	private ArrayList<Books> bk = new ArrayList<Books>();
	public Books(long isbn, String author, long sku, String title,
			double price, int qty){
		super(sku, title, price, qty);
		this.isbn = isbn;
		this.author = author;
	}
	
/*	public void addProduct(Books b) {
		bk.add(b);
	}
	public void removeProduct(Books b) {
		bk.remove(b);
	}*/
	public String displayProduct() {
		//return "Book\t" + super.displayProduct() + "\t" + isbn + "\t" + author;
		return super.displayProduct() + "isbn="+isbn + "\n" + "author=" + author + "\n";
	}
	public String displaySort() {
		return "Book\t" + super.displaySort();
	}
public void displayTable() {
		for(Books b : bk) {
			System.out.println(b);
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
		  totprice = getPrice()*getQuantity();
		  System.out.println("Price: " + getPrice() + "\tQuantity: " + getQuantity() + "\n");
		  shcred = 3.99*getQuantity();
		  totshcred = shcred*getQuantity();
		  totcomm = (.15*getQuantity());
		  profit =  totprice + totshcred - (totcomm+co);
		  System.out.println("Total Price: $" + totprice + "\n" + "Total Shipping Credit: $"
		  + totshcred +  "\n" + "Total Commision: $" + totcomm + "\n"
				  + "Profit: $" + profit + "\t");
	}
	
	
}
