
import java.util.Scanner;

public class Semana3 {
    public static void main(String[] args) {
        //var x = 5;
        //var y = x;
        //y = y+5;
        //System.out.println(y);
        //System.out.println(x);

        //metodos toUpperCase(String) y toLowerCase(string)

        // Metodo concat()
        //String firstName = "Juan";

        // Scanner
        
        // Ejecicio en clase-> Saludo personal

        // Scanner scan = new Scanner(System.in);
        // System.out.println("Ingrese su nombre: ");
        // String  nombre = scan.nextLine();
        // System.out.println("Bienvenido "+ nombre);

        // Ejecicio en clase-> Area circuo

        //Scanner entrada = new Scanner(System.in);
        //System.out.println("Ingrese el radio del circulo: ");
        //entrada.useLocale(Locale.US); //--> Con esto toma los double (Y no sé que mas) solo cuando se usa punto('.')
        //                               -//sin esta linea solo los toma al usar la coma(',')
        //double radio = entrada.nextDouble();
        //double area = Math.PI * Math.pow(radio, 2);//radio*radio*3.14;
        //System.out.println("El radio del circulo es: " + area);
        
        Scanner entrada = new Scanner(System.in);
        System.out.println("Ingrese el valor de A: ");
        double a = entrada.nextDouble();
        System.out.println("Ingrese el valor de B: ");
        double b = entrada.nextDouble();
        System.out.println("Ingrese el valor de C: ");
        double c = entrada.nextDouble();
        //Ecuacion para encontrar x's de una ecuacion de segundo grado : -b +- raiz(b**2 + 4*a*c)/2a
        double discriminante = Math.pow(b, 2) - (4*a*c);

        if (discriminante >= 0){
            double x1 = (((-b) + Math.sqrt(discriminante))/(2*a));
            double x2 = (((-b) - Math.sqrt(discriminante))/(2*a));
            System.out.println("El valor de x1 es: "+x1+" y el de x2 es: "+x2);
        }else {
            System.out.println("La ecuacion no tiene solución en los reales");
        }
    }
}
