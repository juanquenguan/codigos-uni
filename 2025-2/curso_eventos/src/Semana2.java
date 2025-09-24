//En este archivo escribire lo que vea en la clase de F.P.O.E en la semana 2


public class Semana2 {
        /*
    public static void main(String[] args){
        ArrayList<String>nombres = new ArrayList<>();
        nombres.add("Ana");
        nombres.add("Luis");
        nombres.add("Carlos");
        for(String n : nombres) {
            System.out.println(n);
        }
        System.out.println(3);
        System.out.println(358);
        System.out.println(5000);
        System.out.println(3+3);
        System.out.println(2*5);
    }
        */
    /*Mostrar resultado de las operaciones de dos números 
    public static void main(String[] args) {
        //Declarar las variables
        int num1 = 200, num2 = 35;

        //Imprimir las operaciones
        System.out.println("El resultado de la suma es: "+ (num1 + num2));
        System.out.println("El resultado de la resta es: "+ (num1 - num2));
        System.out.println("El resultado de la multiplicación es: "+ (num1 * num2));
        System.out.println("El resultado de la división es: "+ (num1 / num2));
    }*/
    //Mostrar el mayor de dos números
    public static void main(String[] args) {
        //Declarar las variables
        int num1 = 20, num2 = 20;

        if (num1 >= num2) {
            if (num1 == num2) {
                System.err.println("Los números " + num1 + " y " + num2 + " son iguales");  
            }else{
                System.err.println(num1 + " es mayor que " + num2);  
            }
        }else{
            System.err.println(num2 + " es mayor que " + num1);
        }
    }
}
