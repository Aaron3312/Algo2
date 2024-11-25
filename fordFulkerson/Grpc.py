syntax = "proto3";

// Mensaje para la petición que contiene dos números
message CalculatorRequest {
    int32 first_number = 1;
    int32 second_number = 2;
}

// Mensaje para la respuesta que contiene el resultado
message CalculatorResponse {
    int32 result = 1;
}

// Definición del servicio Calculator
service Calculator {
    // Un RPC simple que recibe dos números y retorna un resultado
    rpc Calculate(CalculatorRequest) returns (CalculatorResponse) {}
}