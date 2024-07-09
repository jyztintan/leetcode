#include <vector>
using namespace std;

class Solution {
public:
    double averageWaitingTime(vector<vector<int>>& customers) {
        
        // Keeps track of total waiting time
        double wait = 0;

        // Keeps track of current chef's business
        int chef = 1;

        for (vector<int> customer: customers) {

            /*
            For every customer there are 2 scenarios:
            1) The chef was already available so when this customer comes in, he will cook immediately upon arrival
            2) The chef was already busy, so we just add on the new customer 's order onto the chef' s schedule
            */
            if (customer[0] >= chef) {
                chef = customer[0] + customer[1];
            } else {
                chef += customer[1];
            }

            
            // The chef's status is now updated to when this customer' s meal will be ready
            // Hence, we just need to sum the difference between this and their respective arrival time
            wait += chef - customer[0];
        }

        return wait / customers.size();
    }
};
