%% Control Torque of IPMSM Inside Axle-Drive EV in DQ Frame
% 
% This example models an interior permanent magnet synchronous machine
% (IPMSM) propelling a simplified axle-drive electric vehicle. The example 
% controls and simulates the torque in the rotor direct-quadrature (DQ) 
% reference frame. The IPMSM operates in both motoring and generating 
% modes. A fixed-ratio gear-reduction model implements the vehicle 
% transmission and differential. The |Vehicle Controller| subsystem 
% converts the driver inputs into a relevant torque command. The |Drive 
% Controller| subsystem controls the torque of the IPMSM. The control
% algorithm is implemented in continuous time. To simulate this model 
% faster, this example uses a variable-step solver. The |Scopes| subsystem 
% contains scopes that allow you to see the simulation results.
% 

% Copyright 2024 The MathWorks, Inc.



%% Open Model

open_system('IPMSMAxleDriveEVDQ')

set_param(find_system('IPMSMAxleDriveEVDQ','FindAll', 'on','type','annotation','Tag','ModelFeatures'),'Interpreter','off')

%% Open Electric Drive Subsystem

set_param('IPMSMAxleDriveEVDQ/Electric Drive','LinkStatus','none')
open_system('IPMSMAxleDriveEVDQ/Electric Drive','force')

%% View Simulation Results from Simscape Logging
%%
%
% This plot shows the requested and estimated torque for the
% test as well as the DQ currents in the electric drive.
%


IPMSMAxleDriveEVDQPlotMotorTorque;

%%

