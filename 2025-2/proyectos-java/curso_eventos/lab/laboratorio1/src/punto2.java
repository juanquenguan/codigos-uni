/*
 * Autor: Juan Quenguan
 * Código: 2460557
 * Punto 2 - laboratorio 1
 */
import java.util.*;

public class punto2 {
    public static String determinarCategoria(int edad) { //metodo solicitado
        if (edad < 12) return "Infantil";
        else if (edad < 18) return "Juvenil";
        else return "Mayores";
    }

        //metodo solicitado
    public static int calcularPago(String categoria, int meses, Map<String, Integer> tarifas) {
        return tarifas.get(categoria) * meses;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Map<String, Integer> tarifas = new HashMap<>();// Un mapa de duplas para las tarifas
        tarifas.put("Infantil", 43000);
        tarifas.put("Juvenil", 36000);
        tarifas.put("Mayores", 32000);
        int cantidad;
        do{//Validador de que hayan al menos 3 personas
        System.out.print("¿Para cuántas personas?: ");
        cantidad = scanner.nextInt(); scanner.nextLine();
        if (cantidad < 3) {
            System.out.println("Personas insuficientes.");
        }
        }while(cantidad < 3);

        for (int i = 0; i < cantidad; i++) {
            System.out.println("Persona " + (i + 1));
            System.out.print("Nombre: ");
            String nombre = scanner.nextLine();
            System.out.print("Edad: ");
            int edad = scanner.nextInt();
            System.out.print("Meses a pagar: ");
            int meses = scanner.nextInt(); scanner.nextLine();

            if (edad > 0 && meses > 0) {// validación
                String cat = determinarCategoria(edad);
                int total = calcularPago(cat, meses, tarifas);
                System.out.println(nombre + " - " + cat + " - Total: $" + total);
            } else {
                System.out.println("Datos inválidos.");
            }
        }
    }
}
