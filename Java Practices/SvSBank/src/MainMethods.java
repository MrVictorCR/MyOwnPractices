import java.util.HashMap;
import javax.swing.JOptionPane;

public class MainMethods{
    
    Menu methodMenu = new Menu();
    Customer methodCustomer = new Customer();
    EndProgram methodsEndProgram = new EndProgram();
    CustomerTest methodsCusTes = new CustomerTest();
    
    // Variables
    private HashMap <String, Object> mapCustomer = new HashMap <String, Object> ();
    private String xAccountNumber;
    private String xSetNameStr;

    // Methods

        // RegisterCustomer
        public void registerNewCustomer(){
            while (methodCustomer.isProgramContinue()){ // Create if for the data 'if that is correct'

                xSetNameStr = (String) JOptionPane.showInputDialog(null, "Create your Username:");
                xAccountNumber = (String) JOptionPane.showInputDialog(null, "What is your account number?");
                methodCustomer.setProgramContinue(false);
                // Adding the new Customer
                mapCustomer.put(xAccountNumber, xSetNameStr);
                methodCustomer.setAccountNumber(xAccountNumber);
                methodCustomer.setName(xSetNameStr);
                
                JOptionPane.showMessageDialog(null, "Account successfully created " + xSetNameStr);
                getCustomer();
                // methodMenu.mainMenu();

                
            }       
        }
        // LoginCustomer
        public void getCustomer(){
            String accountNumberConfirm = (String) JOptionPane.showInputDialog(null, "What is your account number?",
                                           "Login", 0);
            String accountNCStr = (accountNumberConfirm).toString();
            if (mapCustomer.containsKey(accountNCStr)){
                methodsCusTes.methodsCustomerMenu();
            } else { // Make an Exception
                JOptionPane.showMessageDialog(null, "Program finished");
                System.exit(0);
            }

        }
            // Getters and Setters

                // HashMap
                public HashMap<String, Object> getMapCustomer() {
                    return mapCustomer;
                }

                public void setNewMap(HashMap<String, Object> mapCustomer) {
                    this.mapCustomer = mapCustomer;
                }

            
                // xAccountNumber
                public String getxAccountNumber() {
                    return xAccountNumber;
                }
                public void setxAccountNumber(String xAccountNumber) {
                    this.xAccountNumber = xAccountNumber;
                }

                // xSetNameStr
                public String getxSetNameStr() {
                    return xSetNameStr;
                }
            
            
                public void setxSetNameStr(String xSetNameStr) {
                    this.xSetNameStr = xSetNameStr;
                }
}


