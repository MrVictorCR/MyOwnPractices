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
        public void registerNewCustomer() throws NumberFormatException{
            while (methodCustomer.isProgramContinue()){ 

                xSetNameStr = (String) JOptionPane.showInputDialog(null, "Create your Username:");
                xAccountNumber = (String) JOptionPane.showInputDialog(null, "What is your account number?");

                int AccountConditional = Integer.parseInt(xAccountNumber);
                if (AccountConditional != 0){
                    // Adding the new Customer
                    mapCustomer.put(xAccountNumber, xSetNameStr);
                    methodCustomer.setAccountNumber(xAccountNumber);
                    methodCustomer.setName(xSetNameStr);
                    JOptionPane.showMessageDialog(null, "Account successfully created " + xSetNameStr);
                    methodCustomer.setProgramContinue(false);

                    try {
                        getCustomer();
                    } catch (NoneexistAccountException nae) {
                        JOptionPane.showMessageDialog(null, "There is no account registered with that account number");
                    } catch (NumberFormatException nfe){
                        JOptionPane.showMessageDialog(null, "Invalid Value");
                    }
                } 
            }       
        }

        // LoginCustomer
        public void getCustomer() throws NoneexistAccountException, NumberFormatException{
            String accountNumberConfirm = (String) JOptionPane.showInputDialog(null, "What is your account number?",
                                           "Login", 0);
            int accountNCint = Integer.parseInt(accountNumberConfirm);
            if (accountNCint > 0){   
                String accountNCStr = (accountNumberConfirm).toString();
                if (mapCustomer.containsKey(accountNCStr)){
                    methodsCusTes.methodsCustomerMenu();
                } else {
                    throw new NoneexistAccountException();
                } 
            } else {
                throw new NumberFormatException();
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


