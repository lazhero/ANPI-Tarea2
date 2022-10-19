function mainProgram()
  p=q=[1:0.1:25]';
  m=242;
  trid=getTridiagonal(p,q,m);
  b=ones(m,1);
  var=jacobi(trid,b,b,1000,1e-10)

endfunction
