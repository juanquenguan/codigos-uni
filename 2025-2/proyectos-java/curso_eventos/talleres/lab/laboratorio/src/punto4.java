/*
 * Autor: Juan Quenguan
 * Código: 2460557
 * Punto 4 - laboratorio 1
 */
import java.util.*;

public class punto4 {
    public static boolean validar(String expr) {
        Deque<Character> pila = new ArrayDeque<>();
        Map<Character, Character> pares = Map.of(')', '(', '}', '{', ']', '[');

        for (char cadena : expr.toCharArray()) {
            if (pares.containsValue(cadena)) pila.push(cadena);
            else if (pares.containsKey(cadena)) {
                if (pila.isEmpty() || pila.pop() != pares.get(cadena)) return false;
            }
        }
        return pila.isEmpty();
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Ingrese expresión: ");
        String frase = scanner.nextLine();
        if (validar(frase)) System.out.println("VÁLIDO");
        else System.out.println("INVÁLIDO");
    }
}
