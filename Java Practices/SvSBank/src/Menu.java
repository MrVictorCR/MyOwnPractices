import javax.swing.JOptionPane;

public class Menu{

    EndProgram methodEnd = new EndProgram();
    

    public int mainMenu(){

        Object [] options = {"Login", "Sign up", "Exit"};
        int choose = JOptionPane.showOptionDialog(null,"What do you want to do?", "Welcome to SvSBank",
                     JOptionPane.DEFAULT_OPTION, JOptionPane.PLAIN_MESSAGE,null, options, options[0]); 
        
        return choose;
    }

    // A posible problem occurs here
    public int customerMenu(){

        // String xString = methodsMain.getxSetNameStr();
        Object [] cmrOptions = {"Deposit", "Withdraw", "Your Balance" ,"Exit"};
        int cmrChooseMenu = JOptionPane.showOptionDialog(null,"What do you want to do?","Welcome back",
                     JOptionPane.DEFAULT_OPTION, JOptionPane.PLAIN_MESSAGE,null, cmrOptions, cmrOptions[0]); 
        
        return cmrChooseMenu;
    }

    public int returnMenu(){

        int returnMenu = 0;

        Object [] returnOptions = {"Yes", "No"};
        returnMenu = JOptionPane.showOptionDialog(null,"Do you want to continue with the program?","",
                     JOptionPane.DEFAULT_OPTION, JOptionPane.PLAIN_MESSAGE,null, returnOptions, returnOptions[0]); 

        return returnMenu;
    }
}