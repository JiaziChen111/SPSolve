function res = SPParsersAvailableQ
res=and(exist('modelezAim.Aim','class')==8,...
exist('trollAim.Aim','class')==8)