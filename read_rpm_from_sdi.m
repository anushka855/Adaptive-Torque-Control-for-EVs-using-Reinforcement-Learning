function rpm = read_rpm_from_sdi()
% Read most recent RPM from SDI
rpm = NaN;
[runIDs, ~] = Simulink.sdi.getAllRunIDs;
if isempty(runIDs), return; end

latestRun = Simulink.sdi.getRun(runIDs(end));

% Try common RPM signal names
candidates = {'motor_rpm','RPM','rpm','shaft_speed','Speed'};
for k = 1:numel(candidates)
    sigIDs = latestRun.getSignalIDsByName(candidates{k});
    if ~isempty(sigIDs)
        sig = latestRun.getSignal(sigIDs(1));
        data = sig.Values.Data;
        if ~isempty(data)
            rpm = data(end);
            return;
        end
    end
end

% Try first signal with RPM pattern
allSignals = latestRun.getSignalIDs();
for id = allSignals
    sig = latestRun.getSignal(id);
    nm = lower(sig.Name);
    if contains(nm,'rpm')
        data = sig.Values.Data;
        if ~isempty(data)
            rpm = data(end);
            return;
        end
    end
end
end
