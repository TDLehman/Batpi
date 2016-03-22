/* Tylor Lehman
 * Radar Map
 * BatPi
 * _____________________________________________________________________________________
 * Object to construct a GUI for the BatPI surroundings
 *
 */

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.*;
import java.lang.*;
import java.io.*;

public class RadarMap{
   private JFrame radarmap;
   

   public RadarMap(){
      JFrame map = new JFrame("RadarMap");
      map.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      map.setSize(600,400);
      map.setLocationRelativeTo(null);
      map.add(makePanel());
      map.add(makeLines());
      map.setVisible(true);
   }
   
   public static JPanel makePanel(){
      JPanel panel = new JPanel();
      panel.setLayout(new BorderLayout());
      panel.setOpaque(true);
      int xdim=600;
      int ydim=400;
      panel.setPreferredSize(new Dimension(xdim, ydim));
      panel.setBackground(Color.BLACK);
      Origin o = new Origin();
      panel.add(o);
      //LinesComponent comp = new LinesComponent();
      //comp.setPreferredSize(new Dimension(320, 200));
      //comp.addLine(xdim/2, ydim-(ydim/8), 30, 30, Color.GREEN);
      //comp.addLine(xdim/2, ydim-(ydim/8), 500, 30, Color.GREEN);
      //panel.add(comp);
      return panel;
   }

   public static JPanel makeLines(){
      JPanel panel = new JPanel();
      panel.setLayout(new BorderLayout());
      panel.setBackground(Color.BLACK);
      panel.setOpaque(true);
      int xdim=600;
      int ydim=400;
      panel.setPreferredSize(new Dimension(xdim, ydim));
 
      //Origin o = new Origin();
      //panel.add(o);
      LinesComponent comp = new LinesComponent();
      comp.setPreferredSize(new Dimension(320, 200));
      comp.addLine(xdim/2, ydim-(ydim/8), 30, 30, Color.GREEN);
      comp.addLine(xdim/2, ydim-(ydim/8), 500, 30, Color.GREEN);
      panel.add(comp);
      return panel;
   }
}




class Origin extends JComponent{
   public void paintComponent(Graphics g){
      super.paintComponent(g);
      g.setColor(Color.GREEN);
      g.fillOval(getWidth()/2, getHeight()-(getHeight()/8), 20, 20); 
        
   }
}

class LinesComponent extends JComponent{
private static class Line{
   final int x1;
   final int y1;
   final int x2;
   final int y2;
   final Color color;
   public Line(int x1, int y1, int x2, int y2, Color color){
      this.x1 = x1;
      this.y1 = y1;
      this.x2 = x2;
      this.y2 = y2;
      this.color = color;
   }
}
private final LinkedList<Line> lines = new LinkedList<Line>();

public void addLine(int x1, int x2, int x3, int x4) {
    addLine(x1, x2, x3, x4, Color.black);
}

public void addLine(int x1, int x2, int x3, int x4, Color color) {
    lines.add(new Line(x1,x2,x3,x4, color));        
    repaint();
}

public void clearLines() {
    lines.clear();
    repaint();
}

@Override
protected void paintComponent(Graphics g) {
    super.paintComponent(g);
    for (Line line : lines) {
        g.setColor(line.color);
        g.drawLine(line.x1, line.y1, line.x2, line.y2);
    }
}

}
