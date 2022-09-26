public class Operaciones {
  public static void main(String[] args) {
    int num1 = 15;
    int num2 = 10;
    int suma = 0;
    System.out.println(num1);
    System.out.println(num2);

    suma = num1 + num2;


    System.out.println(suma);


    if (suma > 10){
        System.out.println("La suma es mayor que 10");
    }
    else if(suma >5 && suma  < 10){
        System.out.println("La suma esta entre 5 y 10");
    }else{
        System.out.println("La suma es menor que 10");
    }


  }
}