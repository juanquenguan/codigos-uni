/*
 * Autor: Juan Quenguan
 * Código: 2460557
 * Punto 1 - laboratorio 1
 */
import java.util.Scanner;

public class punto1 {
    //Método solicitado en el problema
    public static double calcularSubtotal(int cantidad, double precio) {
        return cantidad * precio;
    }

    //Método solicitado en el problema
    public static String formatearNombre(String palabra) {
        return palabra.toUpperCase();
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double total = 0;       // acumulador del total
        int itemsValidos = 0;   // contador de ítems válidos
        char moneda = '$';      // símbolo de la moneda

        System.out.print("¿Cuántos ítems desea ingresar?: ");
        int n = scanner.nextInt();
        scanner.nextLine(); // limpiar buffer

        for (int i = 0; i < n; i++) {
            System.out.println("Ítem " + (i + 1));
            System.out.print("Nombre: ");
            String nombre = scanner.nextLine();
            System.out.print("Cantidad: ");
            int cantidad = scanner.nextInt();
            System.out.print("Precio: ");
            double precio = scanner.nextDouble();
            scanner.nextLine();

            if (cantidad > 0 && precio > 0) {
                double subTotal = calcularSubtotal(cantidad, precio);
                System.out.println(formatearNombre(nombre) + " -> Subtotal: " + moneda + subTotal);
                total += subTotal;
                itemsValidos++;
            } else {
                System.out.println("Datos inválidos, ítem rechazado.");
            }
        }
        System.out.println("Ítems válidos: " + itemsValidos);
        System.out.println("Total a pagar: " + moneda + total);
    }
}
