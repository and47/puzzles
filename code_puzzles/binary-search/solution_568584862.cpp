#include <algorithm>
#include <iostream>
#include <vector>
#include <numeric>


using namespace std;

using namespace std;

    class Solution {
    public:
        int search(vector<int>& nums, int target) {

            vector<int> idxs = nums;
            std::iota(idxs.begin(), idxs.end(), 0);
            
            return(bsearch(nums, idxs, target));
        }

        int bsearch(vector<int> nnums, vector<int> nidxs, int target) {
            int sz = std::size(nnums);

            if (sz < 2) if (nnums[0] == target) return(nidxs[0]); else return(-1);

            int midpoint = sz / 2;
            std::vector<int> numsContainingHalf, idxsContainingHalf;


            std::cout << "Test: " << sz << midpoint << endl;

            if (target < nnums[midpoint]) {
                numsContainingHalf = std::vector<int>(nnums.begin(), nnums.end() - midpoint);
                idxsContainingHalf = std::vector<int>(nidxs.begin(), nidxs.end() - midpoint);
            }
            else {
                numsContainingHalf = std::vector<int>(nnums.begin() + midpoint, nnums.end());
                idxsContainingHalf = std::vector<int>(nidxs.begin() + midpoint, nidxs.end());
            }
            return(bsearch(numsContainingHalf, idxsContainingHalf, target));
        }
    };