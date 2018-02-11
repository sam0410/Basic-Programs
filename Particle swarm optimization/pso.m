clear
close all force
%% Variable declarations

numvar=5;                                  %number of variables
numswarm=50;                               %number of particles in the swarm
iter=1000;                                 %number of iterations of the algo
minvar=-10*ones(1,numvar);                 %minimum value the var can take
maxvar=10*ones(1,numvar);                  %maximum value the var can take
w=1;                                       %inertia coefficient
c1=2;                                      %personal accelaration coefficient
c2=2;                                      %social accelaration coefficient
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
