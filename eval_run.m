function out = eval_run(model,Ts,ep_time,scenario)

load_system(model);

set_param([model '/Inputs'],'ActiveScenario',scenario);

set_param(model,'FastRestart','off');
set_param(model,'StopTime',num2str(ep_time));

set_param(model,'ZeroCrossControl','UseLocalSettings');
set_param(model,'ZeroCrossAlgorithm','Adaptive');

h = init_ev_noedit(model,Ts,0,ep_time);

simOut = sim(model,...
    "StopTime",num2str(ep_time),...
    "ReturnWorkspaceOutputs","on",...
    "SimulationMode","normal");

tor = simOut.torque;
spd = simOut.speed;

tor_s = movmean(tor,7);
spd_s = movmean(spd,7);

N = numel(tor_s);
t = (0:N-1).' * Ts;

out = struct('t',t,'torque',tor_s,'speed',spd_s);
end
