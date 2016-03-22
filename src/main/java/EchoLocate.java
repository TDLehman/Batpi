import org.python.core.PyException;
import org.python.core.PyInteger;
import org.python.core.PyObject;
import org.python.util.PythonInterpreter;


public class EchoLocate{
   public static void main(String[] args) throws PyException{
      //Create python Interpreter
      PythonInterpreter interp = new PythonInterpreter();
      interp.exec("import RPi.GPIO as GPIO");
      interp.exec("import time");
      interp.exec("GPIO.setmode(GPIO.BCM)");
      interp.exec("trig = 23");
      interp.exec("echo = 24");
      interp.exec("GPIO.setup(trig, GPIO.OUT)");
      interp.exec("GPIO.setup(echo, GPIO.IN)");
      interp.exec("GPIO.output(trig, false)");
      interp.exec("time.sleep(.5)");
      interp.exec("GPIO.output(trig, TRUE)");
      interp.exec("time.sleep(0.00001)");
      interp.exec("GPIO.output(trig, FALSE)");
      interp.exec("while GPIO.input(echo) == 0:");
      interp.exec("  start = time.time()");
      interp.exec("while GPIO.input(echo) == 1:");
      interp.exec("  end = time.time()");
      interp.exec("duration = end - start");
      interp.exec("soundSpeed = 34300");
      interp.exec("distance = duration*34300/2");
      interp.exec("GPIO.cleanup()");
      interp.exec("return distance");
   }
}
