bool is_prime(long n){
    loop(2, sqrt(n) + 1, 1){
        if(n % i == 0)
            return false;
    }
    return true;
}
int pri_factorisation(long n){
    int length = 0;
    int i = 2;
    while(n != 1){
        if(n % i == 0){
            length += 1;
            while(n % i == 0){
                n = n / i;
            }
        }
        i += 1;
    }
    return length;
}
int main() {
    IO;
    long n = 2;
    while(1){
        pnor(n);
        if(pri_factorisation(n + 3) == 4){
            if(pri_factorisation(n + 2) == 4){
                if(pri_factorisation(n + 1) == 4){
                    if(pri_factorisation(n) == 4){
                        pans(n);
                        break;
                    }else n += 1;
                }else n += 2;
            }else n += 3;
        } else
            n += 4;
    }
    return 0;
}