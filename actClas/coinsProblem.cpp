#include <iostream>
#include <vector>

using namespace std;

int changes(int amount, vector<int>& coins, int index) {
    //we need to encounter the way to 
    /*Input: amount = 5, coins = [1,2,5]
    Output: 4*/
    if (amount - coins[0] == 0) {
        return 1;
    }
    else if (amount - coins[0] < 0) {
        return 0;
    }
    else {
        return changes(amount - coins[0], coins, index) ;
    }
    
}
class Solution {
public:
    int change(int amount, vector<int>& coins) {
        //we need to encounter the way to 
        /*Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1*/




        
        
    }
};

int main() {
    int amount = 5;
    vector<int> coins = {1, 2, 5};
    Solution sol;
    cout << sol.change(amount, coins) << endl;
    return 0;
}