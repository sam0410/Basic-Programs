params.numvar=5;                                  
params.numswarm=50;                               
params.iter=1000;                                 
params.minvar=-10*ones(1,params.numvar);                 
params.maxvar=10*ones(1,params.numvar);                  
params.w=1;                                       
params.c1=2;                                      
params.c2=2; 

Xfinal=pso( params )