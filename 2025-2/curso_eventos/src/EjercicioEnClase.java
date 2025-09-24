/*
 * Estudiante: Juan Paulo Quenguan
 * Código: 2460557
 * Curso: Fundamentos de programacion orietada a eventos
 */

import java.util.ArrayList;
import java.util.Scanner;

public class EjercicioEnClase {
    public static void main (String[]args){
        double entra = 0;
        // Creamos una lista para almacenar números hasta que inserten un -1
        ArrayList<Double> untillMinusOne = new ArrayList<>();
        do { 
            Scanner entrada = new Scanner(System.in);
            System.out.println("Ingrese un número: ");
            double numero = entrada.nextDouble();
            untillMinusOne.add(numero);
            entra = numero;

        } while (entra!= (-1));
       
        // Mostramos la suma de los datos
        double suma = 0;
        for (double item: untillMinusOne) {
             suma = suma +item;
        }
        System.out.println(suma);
    }
}
