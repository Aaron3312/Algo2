public class Car {
    private String model; // Encapsulation: private variable
    public Car(String model) {
    this.model = model;
    }
    public void displayModel() {
    System.out.println("Car model: " + model);
    }
   }
   class ElectricCar extends Car { // Inheritance
    private int batteryLife;
    public ElectricCar(String model, int batteryLife) {
    super(model);
    this.batteryLife = batteryLife;
    }
    public void displayBatteryLife() {
    System.out.println("Battery life: " + batteryLife + " hours");
    }
   }