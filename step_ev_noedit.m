function out = step_ev_noedit(h, acc, brk, incline_deg, wind_mps)
assignin('base','Acc',acc);
assignin('base','Brk',brk);
assignin('base','In',incline_deg);
assignin('base','Wi',wind_mps);

sIn = Simulink.SimulationInput(h.model);
sIn = sIn.setModelParameter('StartTime',num2str(h.t), ...
                            'StopTime', num2str(h.t + h.Ts));
simOut = sim(sIn);
h.t = h.t + h.Ts;

L = [];
if isprop(simOut,'logsout'), L = simOut.logsout; end

names = {};
if isa(L,'Simulink.SimulationData.Dataset')
    names = cell(1,L.numElements);
    for i = 1:L.numElements
        names{i} = L.getElement(i).Name;
    end
end

% --- torque: look for common names
Treq = pick_scan(L, {'visEM.trqR','torque_ref'}, 0);
Te   = pick_scan(L, {'visEM.trqEst','torque_estim'}, 0);

% --- speed
w = 0;
rpm = pick_scan(L, {'visEM.rpm','rpm', ...
    'Measured rotor mechanical velocity [rpm]', ...
    sprintf('Measured rotor\nmechanical velocity [rpm]')}, 0);

if rpm > 0
    w = rpm * 2*pi/60;
end

% ✅ Clamp invalid values to zero:
if isnan(Treq) || isinf(Treq), Treq = 0; end
if isnan(Te)   || isinf(Te),   Te = 0; end
if isnan(w)    || isinf(w),    w = 0; end

Pbat = NaN;

out = struct('h',h,'names',{names},'Te',Te,'w',w,'Pbat',Pbat, ...
             'Treq',Treq,'done',h.t >= h.t_end);
end

% ----- helper: scan dataset safely -----
function v = pick_scan(ds, keys, defaultVal)
v = defaultVal;
if isa(ds,'Simulink.SimulationData.Dataset')
    for i = 1:ds.numElements
        e = ds.getElement(i);
        if ~isempty(e.Values) && ~isempty(e.Values.Data)
            nm = e.Name;
            for k = 1:numel(keys)
                if strcmp(nm, keys{k})
                    d = e.Values.Data;
                    v = d(end);
                    return;
                end
            end
        end
    end
end
end
