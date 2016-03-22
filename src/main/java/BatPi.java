//Tylor Lehman
//BatPi
//BatPi
import java.io.*;
//import org.python.core.PyException;
//import org.python.core.PyInteger;
//import org.python.core.PyObject;
//import org.python.util.PythonInterpreter;

public class BatPi{
   public static void main(String[] args){
      String s = "";
      if (args[0] != null){
         RadarMap map = new RadarMap();
      }
      try{
         //Process p = Runtime.getRuntime().exec("python3 ./main/python/pyTest.py");
         Process p = Runtime.getRuntime().exec("ls");
         BufferedReader stdInput = new BufferedReader(new
                 InputStreamReader(p.getInputStream()));   
         
         
         //read output from the python command (I hope):
         
         System.out.println("Here is your output:\n");
         
         while ((s = stdInput.readLine()) != null){
            System.out.println(s);
         }
         
      }catch(IOException e){
         System.out.print("Exception happened - Here's what I know: \n");
         e.printStackTrace();
         System.exit(-1);
      }
      

      
      
      
   }

}
