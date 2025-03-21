public class ExceptionHandlingExample {
    public static void main(String[] args) {
    try {
    int result = 10 / 0; // This will throw an ArithmeticException
    System.out.println(result);
    } catch (ArithmeticException e) {
    System.out.println("Error: Division by zero!");
    } finally {
    System.out.println("This block always runs.");
    }
    }