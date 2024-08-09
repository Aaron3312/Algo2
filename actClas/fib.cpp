 #include <iostream>
#include <algorithm>

using namespace std;

// Funcion de fibonacci



// double fibs(double n){

//     if (n <= 1){
//         return n;
//     }else if (n == 2){
//         return 1;
//     }else if (n == 3){
//         return 2;
//     }else if (n == 4){
//         return 3;
//     }else if (n == 5){
//         return 5;
//     }else if (n == 6){
//         return 8;
//     }else{
//         return(fibs(n-1) + fibs (n-2));
//     }
// }
#include <iostream>
#include <vector>

long long int fibonacci(long long int n) {
    if (n <= 1) return n;

    std::vector<long long int> fib(n + 1);
    fib[0] = 0;
    fib[1] = 1;

    for (long long int i = 2; i <= n; i++) {
        fib[i] = fib[i - 1] + fib[i - 2];
    }

    return fib[n];
}

int main() {
    long long int n;
    std::cout << "Enter the position of the Fibonacci number: ";
    std::cin >> n;

    long long int result = fibonacci(n);
    std::cout << "Fibonacci number at position " << n << " is: " << result << std::endl;

    return 0;
}


