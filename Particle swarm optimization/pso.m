function [ Xfinal ] = pso( params )
%% Variable declarations

numvar=params.numvar;                      %number of variables
numswarm=params.numswarm;                  %number of particles in the swarm
iter=params.iter;                          %number of iterations of the algo
minvar=params.minvar;                      %minimum value the var can take
maxvar=params.maxvar;                      %maximum value the var can take
w=params.w;                                %inertia coefficient
c1=params.c1;                              %personal accelaration coefficient
c2=params.c2;                              %social accelaration coefficient

singleParticle.x=[];                       %position of the particle
singleParticle.cost=[];                    %cost of the particle
singleParticle.velocity=[];                %velocity of the particle
singleParticle.bestCost=[];                %lowest cost of particle
singleParticle.bestPos=[];                 %position of lowest cost of the particle
particles= repmat(singleParticle,numswarm,1);   %define swarm of particles
globalBestCost=inf;                             %lowest cost among all the particles
globalBestPos=zeros(1,numvar);                  %position having lowest cost among all the particles
%% Initialize the swarm
for i=1:numswarm
    particles(i).x=minvar+(maxvar-minvar).*rand(1,numvar);
    particles(i).cost= CostFunction(particles(i).x);
    particles(i).velocity= zeros(1,numvar); 
    particles(i).bestPos=particles(i).x;
    particles(i).bestCost=particles(i).cost;
    if particles(i).cost < globalBestCost 
        globalBestCost=particles(i).cost;
        globalBestPos=particles(i).x;
    end
end
%% PSO Algorithm
for j=1:iter
for i=1:numswarm
    
    particles(i).velocity= w*particles(i).velocity +...
        c1*(rand(1,numvar)).*(particles(i).bestPos-particles(i).x)...
        + c2*(rand(1,numvar)).*(globalBestPos-particles(i).x);
    
    particles(i).x=particles(i).velocity+particles(i).x;
    particles(i).cost= CostFunction(particles(i).x);
    
    if particles(i).cost < particles(i).bestCost
        particles(i).bestCost=particles(i).cost;
        particles(i).bestPos=particles(i).x;
            if particles(i).cost < globalBestCost 
                globalBestCost=particles(i).cost;
                globalBestPos=particles(i).x;
            end
    end
end
    disp("Iteration number: "+num2str(j)+" Cost of particle: "+num2str(globalBestCost))
    w=w*0.98;   %decreasing the inertia coefficient in every iteration
end

Xfinal=globalBestPos;       %optimum position where value of the function is minimum
end