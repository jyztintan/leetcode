#include <vector>
#include <iostream>
using namespace std;

class Solution
{
public:
    double averageWaitingTime(vector<vector<int>> &customers)
    {

        // Keeps track of total waiting time
        double wait = 0;

        // Keeps track of current chef's business
        int chef = 1;

        for (int i = 0; i < customers.size(); i++)
        {

            /*
            For every customer there are 2 scenarios:
            1) The chef was already available so when this customer comes in, he will cook immediately upon arrival
            2) The chef was already busy, so we just add on the new customer 's order onto the chef' s schedule
            */
            if (customers[i][0] >= chef)
            {
                chef = customers[i][0] + customers[i][1];
            }
            else
            {
                chef += customers[i][1];
            }

            // The chef's status is now updated to when this customer' s meal will be ready
            // Hence, we just need to sum the difference between this and their respective arrival time
            wait += chef - customers[i][0];
        }

        return wait / customers.size();
    }
};

int main()
{
    // Example test case
    vector<vector<int>> customers = {{1, 2}, {2, 5}, {4, 3}};
    Solution sol;
    double result = sol.averageWaitingTime(customers);
    std::cout << "Average Waiting Time: " << result;
    return 0;
}