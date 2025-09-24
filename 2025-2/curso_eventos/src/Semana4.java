
import java.util.HashMap;
import java.util.Map;

public class Semana4 {
    public static void main(String[] args) {
        /* 
        TreeMap<String, String> agenda = new TreeMap<>();
        agenda.put("Ana", "3151111111");
        agenda.put("Luis", "3202222222");
        agenda.put("Sofía", "3103333333");
        agenda.put("Carlos", "3124444444");
        agenda.put("Beatriz", "3115555555");
        agenda.put("Miguel", "3136666666");
        agenda.put("Zoe", "3147777777");

        System.out.println("Agenda completa:");
        for (Map.Entry<String, String> entry : agenda.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }

        // Contactos de A a L (sin incluir M)
        System.out.println("\nContactos A-L:");
        for (Map.Entry<String, String> entry : agenda.subMap("A", "M").entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }

        // Contactos de M a Z (sin incluir Z)
        System.out.println("\nContactos M-Y:");
        for (Map.Entry<String, String> entry : agenda.subMap("M", "Z").entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }

        // Contactos desde S en adelante
        System.out.println("\nContactos desde S:");
        for (Map.Entry<String, String> entry : agenda.tailMap("S").entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }*/
        Map<String, Double> notasAlumnos = new HashMap<>();
        notasAlumnos.put("Ana", 4.5);
        notasAlumnos.put("Luis", 3.8);
        notasAlumnos.put("Sofía", 4.2);

        double notaAndres = notasAlumnos.get("Andrés");
        System.out.println("La nota de Andrés es: " + notaAndres);

        double notaLuis = notasAlumnos.get("Luis");
        System.out.println("La nota de Luis es: " + notaLuis);

        double notaSofia = notasAlumnos.get("Sofia");
        System.out.println("La nota de Sofía es: " + notaSofia);

        notasAlumnos.put("Andrés", 4.0);
        System.out.println("Nota de los alumnos: ");

        for (Map.Entry<String, Double> entry : notasAlumnos.entrySet()) {
            String nomnbre = entry.getKey();
            Double nota = entry.getValue();
            System.out.println(nomnbre + ": " + nota);
        }
    }
}