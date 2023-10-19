import javax.swing.JOptionPane;

// import java.util.HashMap;


public class Customer{

    Menu methodMenu = new Menu();
    EndProgram methodsEndProgram = new EndProgram();

    private String userName;
    private String accountNumber;
    private int balance;
    private boolean programContinue = true;

    // Getters and Setters
    
        // Balance
        public int getBalance() {
            return balance;
        }
        public void setBalance(int balance) {
            this.balance = balance;
        }

        // Name
        public String getUserName() {
            return userName;
        }
        public void setName(String userName) {
            this.userName = userName;
        }
    
        // AccountNumber
        public String getAccountNumber() {
            return accountNumber;
        }
        public void setAccountNumber(String accountNumber) {
            this.accountNumber = accountNumber;
        }

        // ProgramContinue
        public boolean isProgramContinue() {
            return programContinue;
        }
        public void setProgramContinue(boolean programContinue) {
            this.programContinue = programContinue;
        }
      

    // Methods

    public void deposit(int deposit){
        this.balance += deposit;
    }

    public void withdraw(int deposit) throws InsufficientBalanceException{ 
        if (this.balance < deposit){
            throw new InsufficientBalanceException("InsufficientBalanceException");
        }
        this.balance -= deposit;
    }

    public void balance(){
        JOptionPane.showMessageDialog(null, "Your balance is: " + this.balance);
    }

    // Proof
    public void returnMenu(){

        int returnMenu = methodMenu.returnMenu();
        
            if (returnMenu == 0) { // This if doesn't have an exactly function, but, I think that is just call the boolean again.
                isProgramContinue();
            } else if (returnMenu == 1){
                JOptionPane.showMessageDialog(null, "Thank you for your loyalty");
                methodsEndProgram.endFunction();
            }
    }
       
}
