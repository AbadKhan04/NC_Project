clear; clc;

% Heat Conduction
prompt = {'Length:', 'Thermal Conductivity:', 'Temperature Difference:', 'Time:'};
dlgtitle = 'Heat Conduction Parameters';
dims = [1 35];
definput = {'1', '10', '100', '0.1'};
input_values = inputdlg(prompt, dlgtitle, dims, definput);

length = str2double(input_values{1});
thermal_conductivity = str2double(input_values{2});
temperature_difference = str2double(input_values{3});
time = str2double(input_values{4});

heat_flux = thermal_conductivity * temperature_difference / length;
disp(['Heat flux: ', num2str(heat_flux), ' W/m^2']);

x = linspace(0, length, 100);
y = linspace(temperature_difference, 0, 100); % Approximate solution
exact_solution = temperature_difference * exp(-thermal_conductivity * time / length^2) * ones(size(x));

figure;
plot(x, y, 'b-', x, exact_solution, 'r--');
legend('Approximate Solution', 'Exact Solution');
title('Heat Conduction');
xlabel('X');
ylabel('Y');

% Wave Equation
prompt = {'Frequency:', 'Amplitude:', 'Phase:', 'Time:'};
dlgtitle = 'Wave Equation Parameters';
dims = [1 35];
definput = {'1', '2', '0', '1'};
input_values = inputdlg(prompt, dlgtitle, dims, definput);

frequency = str2double(input_values{1});
amplitude = str2double(input_values{2});
phase = str2double(input_values{3});
time = str2double(input_values{4});

angular_frequency = 2 * pi * frequency;
disp(['Angular frequency: ', num2str(angular_frequency), ' rad/s']);

x = linspace(0, 10, 100);
y = amplitude * sin(angular_frequency * x + phase); % Approximate solution
exact_solution = amplitude * sin(angular_frequency * (x - time)); % Exact solution

figure;
plot(x, y, 'b-', x, exact_solution, 'r--');
legend('Approximate Solution', 'Exact Solution');
title('Wave Equation');
xlabel('X');
ylabel('Y');

% Fluid Flow
prompt = {'Velocity:', 'Pressure:', 'Density:'};
dlgtitle = 'Fluid Flow Parameters';
dims = [1 35];
definput = {'5', '1e5', '1000'};
input_values = inputdlg(prompt, dlgtitle, dims, definput);

velocity = str2double(input_values{1});
pressure = str2double(input_values{2});
density = str2double(input_values{3});

kinetic_energy = 0.5 * density * velocity^2;
disp(['Kinetic energy: ', num2str(kinetic_energy), ' J/kg']);

x = linspace(0, 10, 100);
y = kinetic_energy * ones(size(x)); % Approximate solution
exact_solution = y; % Exact solution is the same as approximate solution

figure;
plot(x, y, 'b-', x, exact_solution, 'r--');
legend('Approximate Solution', 'Exact Solution');
title('Fluid Flow');
xlabel('X');
ylabel('Y');