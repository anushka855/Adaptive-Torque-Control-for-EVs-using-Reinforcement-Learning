function h = init_ev_noedit(model, Ts, t0, t1)
load_system(model);

set_param(model,'SimulationMode','normal');
set_param(model,'FastRestart','off');


% Patch undefined gain so sim runs without workspace vars
try
    blk = [model '/Drive Controller/Outer Loop Control/PMSM Torque Estimator/Gain2'];
    set_param(blk,'Gain','1');
catch
end

h = struct('model',model,'Ts',Ts,'t',t0,'t_end',t1,'x',[]);
end
