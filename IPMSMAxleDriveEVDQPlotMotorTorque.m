% Code to plot simulation results from IPMSMAxleDriveEVDQ
%% Plot Description:
%
% This plot shows the requested and estimated torque for the
% test as well as the DQ currents in the electric drive.

% Copyright 2024-2025 The MathWorks, Inc.

% Generate simulation results if they don't exist
if ~exist('simlog_IPMSMAxleDriveEVDQ', 'var')
    sim('IPMSMAxleDriveEVDQ')
end

% Reuse figure if it exists, else create new figure
if ~exist('h1_IPMSMAxleDriveEVDQ', 'var') || ...
        ~isgraphics(h1_IPMSMAxleDriveEVDQ, 'figure')
    h1_IPMSMAxleDriveEVDQ = figure('Name', 'IPMSMAxleDriveEVDQ');
end
figure(h1_IPMSMAxleDriveEVDQ)
clf(h1_IPMSMAxleDriveEVDQ)

temp_colororder = get(gca,'defaultAxesColorOrder');

% Get simulation results
simlog_t = simlog_IPMSMAxleDriveEVDQ.Vehicle_Dynamics.Vehicle_Mass.v.series.time;
simlog_id = simlog_IPMSMAxleDriveEVDQ.Electric_Drive.Meas_I.Current_Sensor_d.I.series.values('A');
simlog_iq = simlog_IPMSMAxleDriveEVDQ.Electric_Drive.Meas_I.Current_Sensor_q.I.series.values('A');
simlog_trq_ref = logsout_IPMSMAxleDriveEVDQ.get('torque_ref');
simlog_trq_estim = logsout_IPMSMAxleDriveEVDQ.get('torque_estim');
simlog_trq_lim = logsout_IPMSMAxleDriveEVDQ.get('torque_lim');

% Plot results
simlog_handles(1) = subplot(2, 1, 1);
plot(simlog_trq_estim.Values.Time, simlog_trq_estim.Values.Data, 'LineWidth', 2)
hold on
plot(simlog_trq_ref.Values.Time, simlog_trq_ref.Values.Data,'--', 'LineWidth', 2)
plot(simlog_trq_lim.Values.Time, simlog_trq_lim.Values.Data,'-.', 'LineWidth', 2)
plot(simlog_trq_lim.Values.Time, -simlog_trq_lim.Values.Data,'-.', 'LineWidth', 2,'Color', temp_colororder(4,:))
hold off
grid on
title('Motor Torque')
ylabel('Torque (Nm)')
legend({'Estimated','Reference','Limits'},'Location','Best');

simlog_handles(2) = subplot(2, 1, 2)
plot(simlog_t, simlog_id,'LineWidth', 2)
hold on
plot(simlog_t, simlog_iq,'LineWidth', 2)
hold off
grid on
title('DQ Currents')
ylabel('Current (A)')
xlabel('Time (s)')
legend({'D-axis','Q-axis'},'Location','Best');

linkaxes(simlog_handles, 'x')

% Remove temporary variables
clear simlog_t simlog_handles temp_colororder
clear simlog_trq_estim
clear simlog_trq_ref simlog_trq_lim
clear simlog_id simlog_iq
