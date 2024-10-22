# // Online C# Editor for free
# // Write, Edit and Run your C# code using C# Online Compiler

# using System;

# public class Transport{
#     public double FuelCapacity;
#     public string Title;
    
#   public Transport(double fuel, string title){
#         this.FuelCapacity = fuel;
#         this.Title = title;
#     }
# }

# public class Car : Transport {
#     public string Color;
#     public string WheelsResin;
       
#     public Car(double fuel, string title) : base(fuel, title) {
#         this.Color = "#880033";
#         this.WheelsResin = "летняя";
#     }
    
#     override public string ToString(){
#         return $"car is: {this.Title} {this.Color}";
#     }
# }

# public class Boat : Transport {
#     public string Color;
#     public string SeatMaterial;
    
#     public Boat(double fuel, string title, string color, string material) : base(fuel, title) {
#         this.Color = color;
#         this.SeatMaterial = material;
#     }
    
#     override public string ToString(){
#         return $"This is: {this.Title} {this.Color}";
#     }
# }


# public class HelloWorld
# {
#     public static void Main(string[] args)
#     {
#         Transport t0 = new Transport(2, "vzhuh");
#         Car c = new Car(10, "Vspish");
#         var b = new Boat(5, "water pluh", "light-red", "wood");
#         Console.WriteLine(b);
#     }
# }
class Transport:
    def __init__(self, fuel, title):
        self.fuel_capacity = fuel
        self.title = title
    
    def __str__(self) -> str:
        return f'крута {self.fuel_capacity} {self.title}'
        
class Car(Transport):
    def __init__(self, fuel, title, SScolor, HappyWheels):
        super().__init__(fuel, title) 
        self.color = SScolor
        self.wheelsResin = HappyWheels
        
    def Bibika(self): 
        print('woaw')
    
    
class Boat(Transport):
    def __init__(self, fuel:int, title:str, bColor:str, seatMaterial:str):
        super().__init__(fuel,title)
        self.color = bColor
        self.assMaterial = seatMaterial
        
def main():
    car = Car(20, 'ВСпыШ', 'SSКрасный', 'ВесёлыеКолёсики') 
    t = Boat(874, 'ПОБЕГ','ВТОРОЙ_КОРИЧНЕВЫЙ', 'ебать_чугун')
    print(t)
    print(car.wheelsResin, car.title, car.color, car.fuel_capacity)

if __name__ == "__main__":
    main()
