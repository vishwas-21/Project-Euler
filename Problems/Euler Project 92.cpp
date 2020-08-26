#include <bits/stdc++.h>
#define loop(start, end, incre) for(int i = start; i < end; i += incre)
#define vi vector<int>
#define di deque<int>
#define print_vd(vd) loop(0, vd.size(), 1){cout << vd[i] << " ";}cout << "\n"
#define pans(x) cout << "Answer = " << x << "\n";
#define pnor(x) cout << x << "\n";
#define IO ios_base::sync_with_stdio(false);cin.tie(NULL);

using namespace std;
bool chain(long n){
    if(n == 89)
        return true;
    if(n == 1)
        return false;
    long temp = 0;
    while(n != 0){
        temp += ((n % 10) * (n % 10));
        n = n / 10;
    }
    return chain(temp);
}
int main() {
    IO;
    long ans;
    for(long i = 1; i <= 10000000; i += 1){
        if(chain(i)) {
            ans += 1;
        }
    }
    pans(ans);
    return 0;
}
