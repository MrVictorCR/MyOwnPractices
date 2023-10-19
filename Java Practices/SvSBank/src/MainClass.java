public class MainClass  {

        
    public static void main(String[] args) throws Exception {

        MainMethods methodsMain = new MainMethods();
        EndProgram methodsEndProgram = new EndProgram();
        Menu methodMenu = new Menu();
        
        int choose = methodMenu.mainMenu();

        if (choose == 0){
            methodsMain.getCustomer();
            // Make an Exception if you don't Sign up first
        } else if (choose == 1){
            methodsMain.registerNewCustomer();

            methodsMain.getCustomer();
        } else if (choose == 2){
            methodsEndProgram.endFunction();
        } 
    }
}   
