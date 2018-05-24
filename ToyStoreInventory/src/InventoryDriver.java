import java.util.*;
import java.lang.*;

public class InventoryDriver {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ArrayList<Movies> m = new ArrayList<Movies>();
		ArrayList<Books> b = new ArrayList<Books>();
		ArrayList<Toys> t = new ArrayList<Toys>();
		ArrayList<Product> p = new ArrayList<Product>();
		

		Movies mov;
		Books bks;
		Toys tys;
		Product x = null;
		Scanner sc = new Scanner(System.in);
		long upc, sku, isbn, choose;
		String title, author;
		double price, weight;
		int qty;
		int input;
		String type;
		
		Product m2 = new Movies(123456, 1111, "Pulp Fiction", 9.99, 3);
		Product m3 = new Books(654321,"JK Rowling", 2222, "Harry Potter",10.50, 3);
		Product m4 = new Toys(3333, "Lego Blocks", 9.99, 3, 34.99);
		p.add(m2);
		p.add(m3);
		p.add(m4);
		
		//String disp = m2.displayProduct();
		//System.out.println(disp);
		
		do {
		//prompt
		displayMenu();
		System.out.println("Enter your choice: \n");
		
		//user response
		input = sc.nextInt();
		
		//input parameter check
		while(input < 1 || input >7) {
			System.out.println("Invalid input! Enter a choice 1 -7\n");
			displayMenu();
			input = sc.nextInt();
		}
		
		switch(input) {
		case 1: {
			//Add product
			//prompt
			System.out.println("Enter the product type (M - Movie, B- Book"
					+ ", T -Toy)\n");
			sc.nextLine();
			type = sc.nextLine();
			char ch = type.charAt(0);
			ch = Character.toUpperCase(ch);
			System.out.println(ch + "\n");
			
			//input parameter check  --! Not Working !--"
			while(ch != 'M' && ch != 'B' &&
					ch != 'T') {
				if(Character.toUpperCase(ch) != 'M' && Character.toUpperCase(ch) != 'B' &&
						Character.toUpperCase(ch) != 'T') {
						System.out.println("Invalid input! Enter 'M', 'B',"
						+ " or 'T'");
				sc.nextLine();
													}
												}
			if(ch == 'M') {
				System.out.println("Enter the SKU: ");
					sku = sc.nextLong();
					System.out.println("Enter the title: ");
					sc.nextLine();
					title = sc.nextLine();
					System.out.println("Enter the price: ");
					price = sc.nextDouble();
					System.out.println("Enter the quantity: ");
					qty = sc.nextInt();
					System.out.println("Enter the upc: ");
					upc = sc.nextLong();
				//mov = new Movies(upc, sku, title, price, qty);
				//p.add(new Movies(upc, sku, title, price, qty));
			//	p.add(mov);
					Product m1 = new Movies(upc, sku, title, price, qty);
					p.add(m1);
				
					System.out.println("Movie added\n");
					String disp1 = m1.displayProduct();
					System.out.println(disp1);
				}
			
			if(ch == 'B') {
				System.out.println("Enter the SKU: ");
					sku = sc.nextLong();
					System.out.println("Enter the title: ");
					sc.nextLine();
					title = sc.nextLine();
					System.out.println("Enter the price: ");
					price = sc.nextDouble();
					System.out.println("Enter the quantity: ");
					qty = sc.nextInt();
					System.out.println("Enter the isbn: ");
					isbn = sc.nextLong();
					System.out.println("Enter the author: ");
					sc.nextLine();
					author = sc.nextLine();
				//	bks = new Books(isbn, author, sku, title, price, qty);
				//	p.add(new Books(isbn, author, sku, title, price, qty));
				//	Books bok = new Books(isbn, author, sku, title, price, qty);
					Product b1 = new Books(isbn, author, sku, title, price, qty);
					p.add(b1);
					System.out.println("Book added\n");
					String disp2 = b1.displayProduct();
					System.out.println(disp2);
				}
			
			if(ch == 'T') {
				System.out.println("Enter the SKU: ");
					sku = sc.nextLong();
					System.out.println("Enter the title: ");
					sc.nextLine();
					title = sc.nextLine();
					System.out.println("Enter the price: ");
					price = sc.nextDouble();
					System.out.println("Enter the quantity: ");
					qty = sc.nextInt();
					System.out.println("Enter the weight in ounces: ");
					weight = sc.nextDouble();
				//	tys = new Toys(sku, title, price, qty, weight);
				//	p.add(new Toys(sku, title, price, qty, weight)); 
					//p.add(tys);
					Product t1 = new Toys(sku, title, price, qty, weight);
					p.add(t1);
					System.out.println("Toy added\n");
					String disp3 = t1.displayProduct();
					System.out.println(disp3);
					
					
			}
			break;
			}
		
		
		
		case 2: {
			//Remove product
//check if empty
				System.out.println("Enter the SKU of the item to be deleted: \n");
					choose = sc.nextLong();
					if(!p.isEmpty()) {
					for(Product pro : p) {
						if(pro.findSKU(choose)) {
							p.remove(pro);
						System.out.println("Product removed");
						}
						else
							System.out.println("Product not found");
					}
					}
					else
						System.out.println("Cannot remove product! Last one left");
					
					break;
		}
		
		case 3: {
			//Find product by sku
			//displayProduct
			System.out.println("Enter the SKU of the product to be found: \n");
			sku = sc.nextLong();
			System.out.println("SKU: " + sku + "\n");
			int cnt = 1;
			boolean flagd = true;
			for(Product pro2 : p) {
				
				System.out.println("Prod " + cnt + ": " + pro2.getSKU() + "\n");
				cnt+=1;
				if(sku == pro2.getSKU()) {
			String	disp4 = pro2.displayProduct();
					System.out.println(disp4);
					flagd = false;
				}
			}
			if(flagd)
				System.out.println("Could not find SKU");
			break;
		}
		
		case 4: {
			//Display inventory sorted by sku
			
			    // Comparator<Product> comp = x;
			      Collections.sort(p,new productBySKU());
			      for(Product pro3: p) {
			String disp6 = pro3.displaySort();
					System.out.println(disp6);
			      }
			break;
		}
		
		case 5: {
			//Display inventory sorted by title
			//displayTable (title)
			Collections.sort(p);
			for(Product pro4: p) {
				String disp5 = pro4.displaySort();
				System.out.println(disp5);
			}
			break;
		}
		case 6: {
			//Process a sale
			//processSale
			System.out.println("Enter SKU: ");
			sku = sc.nextLong();
			System.out.println("Enter the quantity: ");
			qty = sc.nextInt();
			System.out.println("Enter the shipping cost: ");
			double cost = sc.nextDouble();
			
			for(Product pro6: p) {
			if(pro6.getSKU() == sku) {
			pro6.processSale(qty, cost);
			int temp = pro6.getQuantity();
			pro6.setQuantity(temp - qty);
										}
								}
			break;
		}
		case 7: {
			//Quit the program
			System.out.println("Goodbye\n");
			//quit
		}
		default:
			break;
		
		
			
				}
		}while(input !=7);
		
		
	}
	public static void displayMenu() {
		System.out.println("Online Store Inventory Menu\n" 
				+ "\n1. Add product\n" +
					"2. Remove product\n"+
				    "3. Find product by sku\n" +
					"4. Display inventory sorted by sku\n" +
				    "5. Display inventory sorted by title\n" +
					"6. Process a sale\n" +
				    "7. Quit the program\n");

	}
	
	
	

}


