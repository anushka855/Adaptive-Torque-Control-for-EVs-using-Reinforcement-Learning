%% Parameters for Control Torque of IPMSM Inside Axle-Drive EV in DQ Frame

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

% Copyright 2024 The MathWorks, Inc.

%% Machine Parameters
Pmax = 35000;      % Maximum power                   [W]
Tmax = 205;        % Maximum torque                  [N*m]
Ld   = 0.00024368; % Stator d-axis inductance        [H]
Lq   = 0.00029758; % Stator q-axis inductance        [H]
L0   = 0.00012184; % Stator zero-sequence inductance [H]
Rs   = 0.010087;   % Stator resistance per phase     [Ohm]
psim = 0.04366;    % Permanent magnet flux linkage   [Wb]
p    = 8;          % Number of pole pairs
Jm   = 0.1234;     % Rotor inertia                   [Kg*m^2]

%% High-Voltage Battery Parameters
Cdc  = 0.001;      % DC-link capacitor  [F]
Vnom = 325;        % Nominal DC voltage [V] 
V1   = 300;        % Voltage V1(< Vnom) [V]
AH0  = 280;        % Initial battery charge [hr*A]

%% Control Parameters
Kp_id = 0.8779;     % Proportional gain id controller
Ki_id = 710.3004;   % Integrator gain id controller
Kp_iq = 1.0744;     % Proportional gain iq controller
Ki_iq = 1.0615e+03; % Integrator gain iq controller

%% Current References
load IPMSM35kWCurrentReferences;

%% Vehicle Parameters
Mv    = 1100;   % Vehicle mass                   [kg]
g     = 9.8;    % Gravitational acceleration     [m/s^2]
rho_a = 1.2;    % Air density                    [kg/m^3]
AL    = 0.9;    % Max vehicle cross section area [m^2]
Cd    = 0.4;    % Air drag coefficient           [N*s^2/kg*m]
cr1   = 0.1;    % Rolling coefficient            
cr2   = 0.2;    % Rolling coefficient            
i_t   = 9;      % Gear reduction ratio           
Rw    = 0.3;    % Wheel radius                   [m]
