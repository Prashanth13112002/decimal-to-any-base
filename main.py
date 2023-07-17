class solution:
    def decimal_to_base(self,a,b):
        s=" "
        while(a):
            s=str(a%b)+s
            a//=b
        return s
a1=solution()
a=int(input())
b=int(input())
print(a1.decimal_to_base(a,b))

