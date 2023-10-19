import javax.swing.JOptionPane;

public class CustomerTest {
    
    Customer methodsCustomer = new Customer();
    Menu methodMenu = new Menu();
    EndProgram methodsEndProgram = new EndProgram();

    int xDeposit;


    public void methodsCustomerMenu(){
        while (methodsCustomer.isProgramContinue()){
            int cmrChooseMenu = methodMenu.customerMenu();
        
            if (cmrChooseMenu == 0){
                
                int xDeposit = Integer.parseInt((String) JOptionPane.showInputDialog(null, "How much do you want to deposit: "));
                methodsCustomer.deposit(xDeposit);
                JOptionPane.showMessageDialog(null, "You add " + xDeposit + " in your balance");
                methodsCustomer.returnMenu();
            
            } else if (cmrChooseMenu == 1){
                
                    xDeposit = Integer.parseInt((String) JOptionPane.showInputDialog(null, "How much do you want to withdraw: "));
                    try {
                        methodsCustomer.withdraw(xDeposit);
                    } catch (InsufficientBalanceException ibe) {
                        JOptionPane.showMessageDialog(null, "You have insufficient balance in your account");
                        ibe.printStackTrace();
                        
                    } finally {
                        methodsCustomer.returnMenu();
                    } 
    
            } else if (cmrChooseMenu == 2){
                methodsCustomer.balance();
                methodsCustomer.returnMenu();
            } else if (cmrChooseMenu == 3){
                methodsCustomer.setProgramContinue(false);
                methodsEndProgram.endFunction();
            }
    
        }
    
    }
}

