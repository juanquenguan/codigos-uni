import java.awt.*;
import javax.swing.*;

public class Promedio{
    public static void main(String[] args) {
        JFrame frame = new JFrame("calculadora basica");
        frame.setLayout(new FlowLayout());

        JTextField num1 = new JTextField(4);
        JLabel n1 = new JLabel(" y ");

        JTextField num2 = new JTextField(4);
        JLabel n2 = new JLabel(" y : ");

        JTextField num3 = new JTextField(4);
        

        JButton prom = new JButton("Promedio");
        JLabel resultado = new JLabel("Promedio: ");

        prom.addActionListener(e -> {
            try {
                double a = Double.parseDouble(num1.getText());
                double b = Double.parseDouble(num2.getText());
                double c = Double.parseDouble(num3.getText());
                resultado.setText("resultado: "+ ((a+b+c)/3));
            } catch (NumberFormatException ex) {
                resultado.setText("ingresar numeros validos");
            }
        });

        frame.add(num1);
        frame.add(n1);
        frame.add(num2);
        frame.add(n2);
        frame.add(num3);
        frame.add(prom);
        frame.add(resultado);
       
        frame.setSize(2250, 120);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
}