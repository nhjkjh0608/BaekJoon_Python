a=b=c=d=2;
e=1;
f=g=h=i=j=k=l=m=n=o=p=q=r=0;
exec("a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r=b,a+c,b+d,c+d,a+f,e+g,f+h,g+i,h+j,i+k,j+l,k+m,l,m+o,n+p,o+q,p+r,q+r;"*~-int(input()));
print((n+o+p+q+r)%10**9)
