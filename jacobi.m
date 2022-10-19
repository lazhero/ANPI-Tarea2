function [Xf,iteraciones,error]=jacobi(A,x,b,iterMax,tol)
   m=length(A);
   error=0;
   iteraciones=0;
   sumaParcial=0
   Xf=x;
   for k=1:iterMax
      for i=1:m
        iteraciones=i;
        sumaParcial=0;
          for j=1:m
            sumaParcial+=A(i,j)*x(j,1);
          endfor
        x(i,1)=(1/A(i,i))*(b(i,1)-sumaParcial);

       endfor
       Xf=x;
       error=norm(A*Xf-b)
       if(error<tol)
         break

       endif



   endfor


endfunction
