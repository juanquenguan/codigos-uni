import java.awt.*;
import javax.swing.*;

public class Semana9 {
/*
    // Clase interna que maneja el valor del contador
    static class Contador {
        private int v = 0;
        int get() { return v; }
        void inc() { v++; }
        void reset() { v = 0; }
    }

    public static void main(String[] args) {
        Contador contador = new Contador();

        // Crear ventana principal
        JFrame frame = new JFrame("Contador IVC");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(300, 200);
        frame.setLayout(new FlowLayout());

        // Crear componentes
        JLabel label = new JLabel("Valor: " + contador.get());
        JButton bInc = new JButton("Incrementar");
        JButton bReset = new JButton("Reiniciar");

        // Acción para incrementar
        bInc.addActionListener(e -> {
            contador.inc();
            label.setText("Valor: " + contador.get());
        });

        // Acción para reiniciar
        bReset.addActionListener(e -> {
            contador.reset();
            label.setText("Valor: " + contador.get());
        });

        // Agregar componentes al frame
        frame.add(label);
        frame.add(bInc);
        frame.add(bReset);

        // Mostrar ventana
        frame.setVisible(true);
    }
*/
/*
    public static void main(String[] args) {
        JFrame frame = new JFrame("calculadora basica");
        frame.setLayout(new FlowLayout());
        frame.setSize(250, 150);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JTextField num1 = new JTextField(5);
        JTextField num2 = new JTextField(5);
        JButton sumar = new JButton("Sumar");
        JLabel resultado = new JLabel("Resultado: ");

        sumar.addActionListener(e -> {
            try {
                double a = Double.parseDouble(num1.getText());
                double b = Double.parseDouble(num2.getText());
                resultado.setText("resultado: "+ (a+b));
            } catch (NumberFormatException ex) {
                resultado.setText("ingresar numeros validos");
            }
        });
        frame.add(new JLabel("Número 1:"));
        frame.add(num1);
        frame.add(new JLabel("Número 2:"));
        frame.add(num2);
        frame.add(sumar);
        frame.add(resultado);

        frame.setVisible(true);
    }
*/
    public static void main(String[] args) {
        JFrame frame = new JFrame("calculadora basica");
        frame.setLayout(new FlowLayout());

        JTextField campo = new JTextField(5);
        JButton aF = new JButton("A Farenheit");
        JButton aC = new JButton("A Celsius");
        JLabel lbl = new JLabel("Resultado: ");

        aF.addActionListener(e -> {
            double c = Double.parseDouble(campo.getText());
            lbl.setText("Resultado: "+ (c*9/5+32) + "°F");
        });
        aC.addActionListener(e -> {
            double f = Double.parseDouble(campo.getText());
            lbl.setText("Resultado: "+ ((f -32)*5/9) + "°C");
        });

        frame.add(campo);
        frame.add(aF);
        frame.add(aC);
        frame.add(lbl);
        frame.setSize(250, 120);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }

}

