import math


def grow(dt):
    """Calculates the population vs time for given parameters."""

    rate = 0.1
    p0 = 100

    population = p0
    t = 0
    t_array = [0]
    population_array = [0]

    rdt = rate*dt
    while t < 100:
        population += rdt * population
        t += dt
        if abs(t - round(t, 0)) < dt / 2:
            t_array.append(t)
            population_array.append(population)
    return t_array, population_array

def growslow(dt):
    """Calculates the population vs time for given parameters.
    This function runs slightly slower the grow().  It recalculates rate*dt each time step.
    Since these are both constants, there product could be calculated outside of the
    timestep loop and save one multiplication operation per timestep."""

    rate = 0.1
    p0 = 100

    population = p0
    t = 0
    t_array = [0]
    population_array = [0]

    while t < 100:
        population += rate * dt * population
        t += dt
        if abs(t - round(t, 0)) < dt / 2:
            t_array.append(t)
            population_array.append(population)
    return t_array, population_array


def pop100(dt):
    """"Runs a simulation with the passed value of dt and returns the simulation value at (close to) 100"""
    rate = 0.1
    p0 = 100

    population = p0
    t = 0

    while t < 100:
        population += rate * dt * population
        t += dt
    return population




def grow_constrained(dt,rate,p0,timemax,CarryingCapacity):
    """Calculates the population using a constrained growth model as in module 2.3"""

    population = p0
    t = 0
    t_array = [0]
    population_array = [0]

    while t < timemax:
        Births = rate * population * dt
        Deaths = rate * population/CarryingCapacity * population * dt
        population = population + Births - Deaths
        t += dt
        if abs(t - round(t, 0)) < dt / 2:
            t_array.append(t)
            population_array.append(population)

    return t_array, population_array

def multiple_dose_drug(dt, timemax, dose, interval, halflife, alpha):
    """Calculates blood concentration for multiple dose Dilantin as described in the text"""

    EliminationConstant = - math.log(0.5)/halflife
    drug_in_system = 0
    t = 0
    t_array = [t]
    drug_in_system_array = [drug_in_system]

    while t < timemax:
        if t % interval < dt:                         #if remainder of t/interval is smaller than dt then
            drug_in_system += alpha * dose                #add impulse of drug to system.
        drug_in_system -= EliminationConstant * drug_in_system * dt
        t += dt
        t_array.append(t)
        drug_in_system_array.append(drug_in_system)

    return t_array, drug_in_system_array

def format_plot(a):
    """Format a plot for presenation.  Function takes one parameter, a matplotlib.axes object."""

    goldenratio = 1 / 2 * (1 + math.sqrt(5))  # The next few lines are used for the size of plots
    fsx = 7  # Width (in inches) for the figures.
    fsy = fsx / goldenratio  # Height (in inches) for the figures.

    a.tick_params(labelsize=16)
    a.xaxis.label.set_size(18)
    a.yaxis.label.set_size(18)
    a.title.set_size(20)
    a.legend(fontsize=16)
    a.get_figure().set_size_inches(fsx, fsy)
    a.grid(1)
