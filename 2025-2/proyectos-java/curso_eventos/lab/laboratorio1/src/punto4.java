/*
 * Autor: Juan Quenguan
 * Código: 2460557
 * Punto 4 - laboratorio 1
 */
import java.util.*;

public class punto4 {


    // Método que valida si una expresión está balanceada
    public static boolean validar(String expr) {
        Deque<Character> pila = new ArrayDeque<>();
        // Mapa con los pares de cierre/apertura
        Map<Character, Character> pares = Map.of(')', '(', '}', '{', ']', '[');

        for (char cadena : expr.toCharArray()) {
            if (pares.containsValue(cadena)) {
                pila.push(cadena);// si es apertura, lo metemos a la pila
            }
            else if (pares.containsKey(cadena)) {
                // si es cierre, verificamos que coincida con el último abierto
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
