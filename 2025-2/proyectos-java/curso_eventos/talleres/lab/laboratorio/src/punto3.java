/*
 * Autor: Juan Quenguan
 * Código: 2460557
 * Punto 3 - laboratorio 1
 */
import java.util.Scanner;

public class punto3 {
    // Método solicitado en el problema que define la función 
    public static double funcion(double x) {
        if (x <= 0) return 8 * x * x - 6;
        else return 3 * x + 5;
    }

    public static void main(String[] args) {
        System.out.println("Cálculo de f(x) = 8x^2 - 6, si x <= 0; f(x) = 3x + 5, si x > 0");
        Scanner scanner = new Scanner(System.in);
        for (int i = 0; i < 3; i++) {//Hasta 3 porque es lo solicitado en el enunciado
            System.out.print("Ingrese valor de x: ");
            double x = scanner.nextDouble();
            System.out.println("f(" + x + ") = " + funcion(x));
        }
    }
}
