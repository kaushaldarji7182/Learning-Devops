def check_prime(num):
    for i in range(2,num//2):
        if num%i==0:
            print("not prime")
            return
    
    print("prime")