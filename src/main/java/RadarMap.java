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
   private int xdim = 600;
   private int ydim = 400;

   public RadarMap(){
      JFrame map = new JFrame("RadarMap");
      map.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      map.setSize(xdim+15,400);
      map.setLocationRelativeTo(null);
      map.add(makeLines());
      map.setVisible(true);
   }
   

   //Actually draws everything. I should probably make this better.
   public static JPanel makeLines(){
      JPanel panel = new JPanel();
      panel.setLayout(new BorderLayout());
      panel.setBackground(Color.BLACK);
      panel.setOpaque(true);
      int xdim=600;
      int ydim=400;
      panel.setPreferredSize(new Dimension(xdim, ydim));
      LinesComponent comp = new LinesComponent();
      comp.setPreferredSize(new Dimension(320, 200));
      comp.addLine(xdim/2, ydim-(ydim/8), 10, 60, Color.GREEN);
      comp.addLine(xdim/2, ydim-(ydim/8), 590, 60, Color.GREEN);
      panel.add(comp);
      return panel;
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
      addLine(x1, x2, x3, x4, Color.GREEN);
      repaint();
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

      //NUM OF SAMPLES IS HARDCODED RIGHT HERE!!!!!!!! :
      int numOfSamples = 5;

      g.setColor(Color.GREEN);
      int[] a1 = {300, 200, 400};
      int[] a2 = {350, 200, 200};
      int x = 0; //Simply keeps track of number of Things
      //g.fillOval(300-5, 350-6, 10, 10);
      for (Line line : lines) {
         g.setColor(line.color);
         g.drawLine(line.x1, line.y1, line.x2, line.y2);
         //the array points SHOULD contain this: [x1, y1, x2, y2]
         //getPolygon should be sent 410 as max amplitude. 
         //This will have to be Fixed eventually!

         //x++; 
      }
      for(int i = 0; i<numOfSamples; i++){
         int[] points = getPolygon(numOfSamples, i, 300);
         int[] xValues = {300, points[0], points[2]};
         int[] yValues = {350, points[1], points[3]};
         g.fillPolygon(xValues,yValues, 3);          
      }
//      g.fillOval();
      g.setColor(Color.RED);
      g.fillOval(300-5, 350-6, 10, 10);      
   }

   //get polygon of distance, hardcoded for 5 samples:
   public int[] getPolygon(int numOfSamples, int polnum, int amplitint){
      //int[4] outpoints;
      double amplit = (double) amplitint;
      int a1 = 45+polnum*90/numOfSamples;
      int a2 = 63+polnum*90/numOfSamples;
      double dp1x = 300-amplit*Math.cos(Math.toRadians(a1));
      double dp1y = 300-amplit*Math.sin(Math.toRadians(a1));
      double dp2x = 300-amplit*Math.cos(Math.toRadians(a2));
      double dp2y = 300-amplit*Math.sin(Math.toRadians(a2));
      return new int[]{(int) dp1x, (int)dp1y, (int) dp2x, (int) dp2y};
   }
   
}
