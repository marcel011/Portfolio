import java.util.*;
import java.lang.*;
abstract class Product implements Comparator<Product>, Comparable<Product>{
	private long upc, sku;
	private String title;
	private double price;
	private int qty; 
	private ArrayList<Product> prod = new ArrayList<Product>();
	public Product() {
		sku = 0;
		title = "";
		price = 0.0;
		qty = 0;
	}
	public Product(long sku, String title,
			double price, int qty){ 
	
		this.sku = sku;
		this.title = title;
		this.price = price;
		this.qty = qty;
		prod.add(this);
		
		
	}
	public void addProduct(Product p) {prod.add(p);}
	public void removeProduct(Product p) {prod.remove(p);}
	public String displayProduct() {return "sku="+sku + "\n" + "title="+title +
									"\n" + "price=$"+ price +  "\n" + "quantity="+qty + "\n";}
	
	public boolean findSKU(long sku) {
		for(Product p : prod) {
			if(p.sku == sku) {
				p.displayProduct();
			}
				return true;
		}
		 return false;
	}
	public boolean isProduct(long sku) {
		for(Product p : prod) {
			if(p.sku == sku)
				return true;
		}
		 return false;
	}
	public long getSKU() {
		return sku;
	}
	public String getTitle() {
		return title;
	}
	public double getPrice() {
		return price;
	}
	public int getQuantity() {
		return qty;
	}
	public void setQuantity(int qt) {
		qty = qt;
	}
	public void displayTable() {
		for(Product pd : prod) {
		System.out.println("SKU " + pd.sku +"Title "  + pd.title
				+ "Price " + pd.price + "Quantity " + pd.qty);
		}
		}
	public String displaySort() {
		return sku + "\t" + title +
				"\t" + price +  "\t" + qty + "\n";
	}
	abstract void processSale(int qt, double co);
	


/*public int compare(Product pr, Product qr){
    long lhp = pr.getSKU();
    long rhp = qr.getSKU();
    return (int)(lhp - rhp);
    if (lhp < rhp)
 return -1;
    
    if (lhp == rhp )
    	return 0;
    	
    return 1;
    
	}
*/
public int compareTo(Product d) {
	//return (this.title).compareTo(d.title);
	return title.compareTo(d.title);
}
}
