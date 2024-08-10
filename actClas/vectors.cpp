#include <iostream>
#include <vector>


int main() {
    std::vector<int> items = {1, 2, 3, 4, 5, 5};
    std::cout << items.size() << std::endl;
    items.erase(items.end() - 4);
    items.push_back(20);
    items.push_back(30);
    for (int i = 0; i < items.size(); i++) {
        std::cout << items[i] << std::endl;
    }
    std::cout << items[4] << std::endl;
}