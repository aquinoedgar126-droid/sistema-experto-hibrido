% =========================
% SINTOMAS Y CATEGORIAS
% =========================

sintoma("no enciende", sin_energia).
sintoma("no prende", sin_energia).
sintoma("no hay luces", sin_energia).

sintoma("pantalla negra", sin_video).
sintoma("no da video", sin_video).

sintoma("suena beep", problema_ram).
sintoma("pitidos", problema_ram).

% =========================
% REGLA PRINCIPAL
% =========================

diagnosticar(Sintoma, Categoria) :-
    sintoma(Sintoma, Categoria).
    
% =========================
% COMPONENTES
% =========================

componentes_asociados(sin_energia,
    [fuente, cable_corriente, tarjeta_madre]).

componentes_asociados(sin_video,
    [ram, monitor, tarjeta_video]).

componentes_asociados(problema_ram,
    [ram, slots_ram]).

% =========================
% RECURSION
% =========================

evaluar([]).

evaluar([Cabeza|Cola]) :-
    write('Revisando: '),
    write(Cabeza), nl,
    evaluar(Cola).