function tridiagonal= getTridiagonal(p,q,m)

    p=[0;p];
    q=[q;0];
    tridiagonal=zeros(m);

    for i=1:m
      for j=1:m
        if i==j
          tridiagonal(i,j)=2*p(i)+2*q(i);

        elseif j-i==1
          tridiagonal(i,j)=q(j-1);

        elseif i-j==1
          tridiagonal(i,j)=p(i);

        endif
      endfor
    endfor






endfunction


