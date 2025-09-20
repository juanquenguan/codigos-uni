/*
 * Estudiante: Juan Paulo Quenguan
 * Código: 2460557
 * Curso: Fundamentos de programacion orietada a eventos
 */

import java.util.ArrayList;

public class Ejercicios {
    public static void main (String[]args){
        //Ejercicio de estudiante
        // Creamos una lista para almacenar los datos del estudiante
        ArrayList<String> estudiante = new ArrayList<>();

        // Agregamos los datos
        estudiante.add("Nombre: Juan Lopez");
        estudiante.add("Edad: 21 años");
        estudiante.add("Carrera: Ingeniería de Sistemas");
        estudiante.add("Semestre: 4");
        estudiante.add("Universidad: Universidad del Valle");

        // Mostramos los datos
        for (String dato : estudiante) {
            System.out.println(dato);
        }
        
        
        // Ejercicio del rectangulo:
        int largo = 8, ancho = 5;// Variables para las dimensiones del rectángulo

        // Fórmula: área = largo * ancho
        int area = largo * ancho;

        // Mostramos el resultado
        System.out.println("El área del rectángulo es: " + area);
    }
}
