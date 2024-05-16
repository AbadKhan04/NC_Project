clear; clc; close all;

% Prompt user for initial conditions
velocity = input('Enter the initial velocity (m/s): ');
angle = input('Enter the launch angle (degrees): ');
drag_type = menu('Select the type of drag force', 'Zero Drag', 'Linear Drag', 'Quadratic Drag');

% Constants
g = 9.81; % Acceleration due to gravity (m/s^2)
mass = 1; % Mass of the projectile (kg)
k = 0.1; % Linear drag coefficient
c = 0.1; % Quadratic drag coefficient

% Time range for simulation
t = linspace(0, 10, 100); % Time range (0 to 10 seconds, 100 points)

% Calculate trajectories
switch drag_type
    case 1 % Zero Drag
        x_exact = velocity * cos(deg2rad(angle)) * t;
        y_exact = velocity * sin(deg2rad(angle)) * t - 0.5 * g * t.^2;
        x_approx = x_exact;
        y_approx = y_exact;
    case 2 % Linear Drag
        x_exact = (mass / k) * (1 - exp(-k * t / mass)) * velocity * cos(deg2rad(angle));
        y_exact = (mass / k) * (1 - exp(-k * t / mass)) * velocity * sin(deg2rad(angle)) - (mass / k) * g * t;
        x_approx = velocity * cos(deg2rad(angle)) * t;
        y_approx = velocity * sin(deg2rad(angle)) * t - 0.5 * g * t.^2;
    case 3 % Quadratic Drag
        x_exact = (mass / c) * log(cosh((velocity * cos(deg2rad(angle)) + c * t) / mass));
        y_exact = (mass / c) * (tanh((velocity * sin(deg2rad(angle)) + c * t) / mass) - tanh(velocity * sin(deg2rad(angle)) / mass)) - (g * mass / c) * t;
        x_approx = velocity * cos(deg2rad(angle)) * t;
        y_approx = velocity * sin(deg2rad(angle)) * t - 0.5 * g * t.^2;
end

% Plot trajectories
figure;
plot(x_exact, y_exact, 'b-', 'LineWidth', 2);
hold on;
plot(x_approx, y_approx, 'r--', 'LineWidth', 2);
xlabel('Horizontal Distance (m)');
ylabel('Vertical Distance (m)');
title('Projectile Motion Trajectory');
legend('Exact Solution', 'Approximate Solution (No Drag)');
grid on;

% Compare with Python code
fprintf('Comparing MATLAB and Python results...\n');
% Load Python results (replace with your Python code output)
python_data = load('python_results.mat');

% Compare trajectories
matlab_exact = [x_exact', y_exact'];
matlab_approx = [x_approx', y_approx'];
python_exact = python_data.python_exact;
python_approx = python_data.python_approx;

% Calculate errors
error_exact = sum(sum(abs(matlab_exact - python_exact))) / numel(python_exact);
error_approx = sum(sum(abs(matlab_approx - python_approx))) / numel(python_approx);

fprintf('Error in exact solution: %.6f\n', error_exact);
fprintf('Error in approximate solution: %.6f\n', error_approx);