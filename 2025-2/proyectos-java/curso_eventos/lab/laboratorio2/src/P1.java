/*
 * Autor: Juan Quenguan
 * Fundamentos de programación orientada a eventos
 * Laboratorio 2 - Punto 1
 */

import java.util.*;

public class P1 {
    public static Deque<String> pila = new ArrayDeque<>();
    public static void main(String[] args){

        

        Scanner scanner = new Scanner(System.in);

        int opcion;

        // Menú principal
        do {
            System.out.println("\n--- Navegador Web ---");
            System.out.println("1. Visitar nueva página");
            System.out.println("2. Atrás");
            System.out.println("3. Página actual");
            System.out.println("0. Salir");
            System.out.print("Seleccione una opción: ");
            opcion = scanner.nextInt();
            scanner.nextLine(); // limpiar buffer

            switch (opcion) {
                case 1 -> {
                    System.out.print("Ingrese URL: ");
                    String url = scanner.nextLine();
                    visitar(url);
                }
                //case 2 -> atras();
                //case 3 -> actual();
                case 0 -> System.out.println("Saliendo del navegador...");
                default -> System.out.println("Opción inválida.");
            }
        } while (opcion != 0);

    }
    public static void visitar(String url){
        pila.push(url);

    }
}
