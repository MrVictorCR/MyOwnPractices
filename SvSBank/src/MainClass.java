import javax.swing.JOptionPane;

public class MainClass  {

        
    public static void main(String[] args) {

        MainMethods methodsMain = new MainMethods();
        EndProgram methodsEndProgram = new EndProgram();
        Menu methodMenu = new Menu();
        Customer mC = new Customer();
        
        while (mC.isProgramContinue()){
            int choose = methodMenu.mainMenu();

            if (choose == 0){
                try {
                    methodsMain.getCustomer();
                } catch (NoneexistAccountException nae) {
                    JOptionPane.showMessageDialog(null, "There is no account registered with that account number");
                } catch (NumberFormatException nfe){
                    JOptionPane.showMessageDialog(null, "Invalid Value");
                } finally {
                    mC.returnMenu();
                } 

            } else if (choose == 1){
                try {
                    methodsMain.registerNewCustomer();
                } catch (NumberFormatException tsde) {
                    JOptionPane.showMessageDialog(null, "Your bank account can only contain numbers");
                } finally {
                    mC.returnMenu();
                }
            } else if (choose == 2){
                methodsEndProgram.endFunction();
                mC.setProgramContinue(false);
            }  
        }
            
    }
}   
