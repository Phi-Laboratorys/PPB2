%%  Auswerte-Programm fuer Praktikumsversuch SOLARZELLE
%   Anpassung der Schockley-Gleichung an die Messdaten
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%   Version: 07-2016
%   Autor: Viktor Messerer
%   Vorlage: Mathematika-Skript "schockleygleichung_Praktikum_Neu.nb"
%   Verwendung: Physikalisches Praktikum an der Universitaet Bayreuth
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%  Allgemeine Beschreibung:
%   Diese Matlab-Function soll der Auswertung der im Versuch "Solarzelle"
%   aufgenommenen Messdaten dienen. Durch den Aufruf der Function 
%   ' Solarzelle_Auswertung ', entweder im Command Window oder durch
%   druecken der F5-Taste bei geoeffneter Datei, wird das Programm gestartet.
%   Zuerst oeffnet sich ein Fenster, in dem die Datei mit den Messdaten
%   ausgewaehlt werden soll. Die Messdaten muessen sich in einer 
%   '*.txt'-Datei befinden, links die Spannung in Volt, rechts der Strom in 
%   Ampere, mit Leehrzeichen oder Tabullator getrennt. Die Messdaten werden
%   automatisch aus der Datei eingelesen und mit der Kennlinien-Gleichung 
%   (Gleichung 5 im Skript) gefittet. 
%   Es wird ein Plot mit den Messdaten und der gefitteten Kurve ausgegeben
%   und im gleichen Ordner wie die Messdaten gespeichert. Im
%   Plot stehen die angepassten Parameter. Im Output dieser Function stehen
%   neben den angepassten Parametern (jedoch unter anderen Bezeichnungen)
%   die Fehlergrenzen (diese sind jedoch nicht sehr aussagekraeftig). 
%   Eventuell muessen die Grenzen fuer die Fit-Parameter angepasst werden.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%
function    FitResult   = Solarzelle_Auswertung()
%   Die einzelnen, unten definierten Funktionen werden hier nacheinander
%   aufgerufen. 
[ FilePath , FileName ]         =   ChooseData;
[ MeshData ]                    =   ReadData( FilePath , FileName );
[ DunkHell ]                    =   DunkHellChoose( FileName );
[ FitResult, FitParam ]         =   Anpassen( MeshData , DunkHell );
PlotResults( MeshData , FitResult , FitParam , FilePath , FileName );
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%
function    Cons    = Constants()
%   Hier werden die physikalischen Konstanten in ein structure array
%   abgelegt. Die meisten braucht man nicht, deswegen auskommentiert.
% Cons.BohrMagneton   = 9.27402e-24;      %   (Unit: Joule / Tesla)
% Cons.BohrRadius     = 5.29177e-11;      %   (Unit: Meter)
% Cons.PlanckConstant = 6.62607e-34;      %   (Unit: Joule Second)
% Cons.SpeedOfLight   = 299792458;        %   (Unit: Meter / Second)
% Cons.VacuumPermeability = pi*4e-7;      %   (Unit: (Second Volt)/(Ampere Meter))
% Cons.VacuumPermittivity = (Cons.VacuumPermeability*Cons.SpeedOfLight^2)^-1;
                                        %   (Unit: (Ampere Second)/(Meter Volt))
Cons.ElectronCharge = 1.60218e-19;      %   (Unit: Coulomb)
Cons.BoltzmannConstant  = 1.38065e-23;  %   (Unit: Joule / Kelvin)
% Cons.ElectronMass   = 9.10938e-31;      %   (Unit: Kilogram) 
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%
function    [ FilePath , FileName ] =   ChooseData()
%   Merkt sich den Ordner in dem man das letzte mal eine Datei geoeffnet
%   hat. Oeffnet eine Benutzeroberflaeche in diesem Ordner zum Auswaehlen 
%   der Messdatei.
UsPa    = userpath;
UsPa    = UsPa(1:end);
if exist([UsPa '\ChooseData_lastpath.mat'],'file') == 2
    load([UsPa '\ChooseData_lastpath.mat']);
    if ischar(FilePath) ~= 1
        FilePath = UsPa ;
    end
else
    FilePath = UsPa ;
end
[FileName,FilePath,~] = uigetfile({'*.txt'},'Wählen Sie die ''*.txt'' Datei mit den Messdaten aus.',FilePath,'MultiSelect','off');
if isequal(FileName,0), error('Keine Datei ausgewählt!'), end
[~,~,FileExtension]  = fileparts([ FilePath FileName]);
if isequal(FileExtension,'.txt') ~= 1, error('Keine ''~.txt'' Datei ausgewählt!'), end
if ischar(FilePath) == 1
    save([UsPa '\ChooseData_lastpath.mat'],'FilePath');
end
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%
function    [ MeshData ]    =   ReadData( FilePath , FileName )
%   Hier werden die Messdaten nach Matlab importiert und auf ein structure
%   array aufgeteilt.
DataRaw = dlmread( [ FilePath FileName ] );% , ' ' , 0);
MeshData.Voltage    = DataRaw(:,1);
MeshData.Current    = DataRaw(:,2);
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%
function [ DunkHell ]   = DunkHellChoose( FileName  )
%   Wurde die Solarzelle waerend der Messung nicht beleuchtet, kann man
%   davon ausgehen, dass der Photostrom gleich Null ist.
%   Hier soll man auswaehlen ob es sich um eine Messung mit oder ohne
%   Beleuchtung handelt.
choice = questdlg({'Solarzelle beleuchtet oder Dunkelmessung?',['Ausgewählte Datei: ' FileName ]}, ...
	'Dunkel oder Hell', ...
	'Beleuchtet','Dunkel','Beleuchtet');
switch choice
    case 'Beleuchtet'
        DunkHell = 1;
    case 'Dunkel'
        DunkHell = 0;
end
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%
function    [FitResult , FitParam]  = Anpassen( MeshData , DunkHell )
  Cons    = Constants();
%   Schokley-Gleichung nach I aufgeloest: 
%   Strom   =   (-(JP+JS) * RP+U)/(RP+RS)+(k * T * Lambert_W((e * JS * RP * RS)/(k * (RP+RS) * T)))/(e * RS)

%   Umbenennung fuer den Fit:
%   yData   = Strom ;
%   xData   = Spannung ;
%   a    = StromSaett;
%   b    = StromPhoto;
%   c    = RSerie;
%   d    = RParallel;
%   e    = T;

%   Wurde die Solarzelle waerend der Messung nicht beleuchtet, kann man
%   davon ausgehen, dass der Photostrom gleich Null ist.
%   Hier wird anhand der obrigen Auswahl die obere und untere Grenze fuer
%   den Photo-Strom festgelegt. Handelt es sich um eine Dunkelmessung wird
%   der Photostrom fest auf 0 A beschraenkt.
switch DunkHell
    case 1  %   Hell
IPSP    = 0;
IPLB    = 0;
IPUB    = 4;
    case 0  %   Dunkel
IPSP    = 0;
IPLB    = 0;
IPUB    = 0;
end

[xData, yData] = prepareCurveData( MeshData.Voltage, MeshData.Current );
% zData   = zeros(size(xData));
FitFunc = fittype( ['(-(b+a) * d+x)/(d+c)+(' num2str( Cons.BoltzmannConstant )...
                    ' * e * Lambert_W((' num2str( Cons.ElectronCharge ) ...
                    ' * exp((' num2str( Cons.ElectronCharge ) ' * d * ((b+a) * c+x))/('...
                    num2str( Cons.BoltzmannConstant ) ' * (d+c) * e)) * a * d * c)/('...
                    num2str( Cons.BoltzmannConstant ) ' * (d+c) * e)))/(' num2str( Cons.ElectronCharge ) ' * c);']...
                    , 'independent', 'x', 'dependent', 'y' );
% FitFunc = fittype( ['a* (exp((' num2str(Cons.ElectronCharge) '*(x - c*y))/(' num2str(Cons.BoltzmannConstant) '*e)) - 1) + (x - c*y)/d - b - y']...
%                     , 'independent', {'x','y'}, 'dependent', 'z' ,'coefficients',{'a','b','c','d','e'} );

opts            = fitoptions( 'Method', 'NonlinearLeastSquares' );
opts.Display    = 'Off';
opts.MaxIter    = 4000;
opts.MaxFunEvals= 2000; 
%   Grenzen und Start-Werte des Fits:
opts.Lower      = [0 IPLB 0 0 200];
opts.StartPoint = [0.0001 IPSP 1e-2 1e5 500];
opts.Upper      = [1 IPUB 10 inf 800];
%   Eigentlicher Fit:
[FitResult, ~ ] = fit( xData, yData , FitFunc, opts );
[FitResult, ~ ] = fit( [xData, yData],zData, FitFunc, opts );
FitParam.StromSaett = FitResult.a;
FitParam.StromPhoto = FitResult.b;
FitParam.RSerie     = FitResult.c;
FitParam.RParallel  = FitResult.d;
FitParam.T          = FitResult.e;


end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%
function    PlotResults( MeshData , FitResult , FitParam , FilePath , FileName )
fig1    = figure( 'Name', 'Ergebnis der Anpassung und Messwerte' );
hold on
fig1.Position      = [0 200 1000 500];
fig1.PaperOrientation   = 'landscape';
%   Plot:
ResPlot = plot( FitResult, '-r', MeshData.Voltage, MeshData.Current );
%   zus. Eigenschaften des Plots (ResPlot(1) sind die Messwerte 
%   und ResPlot(2) ist der Fit):
ResPlot(1).Color        = 'blue';
ResPlot(1).Marker       = '.';
ResPlot(1).MarkerSize   = 18;

ResPlot(2).Color    = 'red';
ResPlot(2).LineStyle    = '-';
ResPlot(2).LineWidth    = 1.6;

%   Legende:
Legende         = {'Messwerte', 'Angepasste Kurve'};
leg             = legend(Legende);
leg.FontSize    = 12;
leg.Visible     = 'on';
leg.Location    = 'best';

%   Achsen:
ax      = gca;
%     ax.XLim = [0 1.2];
%     ax.YLim = [0 0.6];
ax.FontSize     = 12;
ax.Box          = 'on';
ax.XGrid        = 'on';
ax.XMinorGrid   = 'off';
ax.YGrid        = 'on';
ax.YMinorGrid   = 'off';

xlab            = xlabel('Spannung / Volt');
xlab.FontSize   = 12;
ylab            = ylabel('Strom / Ampere');
ylab.FontSize   = 12;
tit             = title('Plot: Ergebnis der Anpassung und Messwerte');
tit.FontSize    = 12;
set(gca,'LooseInset',get(gca,'TightInset')) 

%   "Ergebnis"-Box:
anno            = annotation('textbox');
BoxString       ={    'Angepasste Parameter:' ,...
                    [ 'Sättigungs-Strom: ' num2str(FitParam.StromSaett,4) ' A' ],...
                    [ 'Photo-Strom: ' num2str(FitParam.StromPhoto,4) ' A' ]...
                    [ 'Serien-Widerstand ' num2str(FitParam.RSerie,4) ' \Omega' ]...
                    [ 'Parallel-Widerstand ' num2str(FitParam.RParallel,4) ' \Omega' ]...
                    [ 'Temperatur: ' num2str(FitParam.T,4) ' K']};
anno.String         = BoxString;
anno.FontSize       = 12;
anno.FitBoxToText   = 'on';
drawnow 
TextBoxBreite       = get(anno, 'Position');
LegBoxPos           = get(leg, 'Position');
anno.Position       = [ LegBoxPos(1)...
                        LegBoxPos(2)-TextBoxBreite(4)-0.02...
                        TextBoxBreite(3)...
                        TextBoxBreite(4)];
anno.BackgroundColor    = 'white';
hold off

[ ~ , Name , ~ ]    = fileparts( [ FilePath FileName ] );
%   Speichert Plot:
print( fig1 , '-dpdf' , [FilePath '\' Name '_Result_Plot'] );%, '-bestfit' );
%   Speichert Daten der Fitkurve (x:voltage[V],y:current[A]).
FileID              = fopen([FilePath '\' Name '_Result_FitData.txt'],'wt+');
NumPoints           = 400-1;
FitResultData       = [min(MeshData.Voltage):(max(MeshData.Voltage)-min(MeshData.Voltage))/NumPoints:max(MeshData.Voltage);FitResult(min(MeshData.Voltage):(max(MeshData.Voltage)-min(MeshData.Voltage))/NumPoints:max(MeshData.Voltage))'];
                        fprintf(FileID,'%.5f\t%.5f\n',FitResultData);
                        fclose(FileID);
msgbox( {'Plot und x-y-Daten der Fit-Kurve wurde im Ordner', FilePath ,'gespeichert!'} ,'Icon','help')

end