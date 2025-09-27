/*
 * Autor: Juan Quenguan
 * Código: 2460557
 * Punto 5 - laboratorio 1
 */
import java.util.*;

public class punto5 {
    private static Queue<String> cola = new ArrayDeque<>();

    public static void agregar(String nombre) { cola.add(nombre); }
    public static String atender() { return cola.isEmpty() ? "Cola vacía" : cola.poll(); }
    public static String siguiente() { return cola.isEmpty() ? "Cola vacía" : cola.peek(); }
    public static int tamano() { return cola.size(); }
    public static void listar() { System.out.println("Cola: " + cola); }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int opcion;
        do {
            System.out.println("1. Agregar\n2. Atender\n3. Siguiente\n4. Tamaño\n5. Listar\n0. Salir");
            opcion = sc.nextInt(); sc.nextLine();
            switch (opcion) {
                case 1 -> { System.out.print("Nombre: "); agregar(sc.nextLine()); }
                case 2 -> System.out.println("Atendido: " + atender());
                case 3 -> System.out.println("Siguiente: " + siguiente());
                case 4 -> System.out.println("Tamaño: " + tamano());
                case 5 -> listar();
            }
        } while (opcion != 0);
    }
}
