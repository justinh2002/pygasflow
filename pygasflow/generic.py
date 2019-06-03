import numpy as np
from pygasflow.utils.decorators import convert_first_argument

@convert_first_argument
def Sound_Speed(T, R=287.058, gamma=1.4):
    """
    Compute the sound speed for a perfect gas. It also hold for thermally
    perfect as well as calorically perfect gases.

    a = sqrt(gamma * R * T) = sqrt(gamma * P / rho)
    If you have (P, rho) use IdealGas.solve to find T and then call this function for a.

    Parameters
    ----------
        T : array_like
            Temperature. If float, list, tuple is given as input, a conversion
            will be attempted. Must be T >= 0.
        R : float
            Specific Gas Constant. Default is air, R=287.058
        gamma : float
            Specific heats ratio. Default to 1.4. Must be > 1.
    
    Returns
    -------
        out : ndarray
            Sound Speed. 
    """
    assert np.all(T >= 0), "Temperature must be >= 0."
    assert R > 0, "Specific gas constant must be >= 0."
    assert gamma > 1, "Specific heats ratio must be > 1."
    return np.sqrt(gamma * R * T)

@convert_first_argument
def Characteristic_Mach_Number(M, gamma=1.4):
# def M_Star_From_M(M, gamma=1.4):
    """
    Compute the Characteristic Mach number M* from a given M.

    Parameters
    ----------
        M : array_like
            Mach number. If float, list, tuple is given as input, a conversion
            will be attempted.
        gamma : float
            Specific heats ratio. Default to 1.4
    
    Returns
    -------
        M* : array_like
            Characteristic Mach number
    """
    assert np.all(M >= 0), "Mach number must be >= 0."
    assert isinstance(gamma, (float)) and gamma > 1, "The specific heat ratio must be > 1."
    return np.sqrt(M**2 * (gamma + 1) / (2 + M**2 * (gamma - 1)))

@convert_first_argument
def Mach_From_Characteristic_Mach_Number(Ms, gamma):
# def M_From_M_Star(Ms, gamma):
    """
    Compute M from a given Characteristic Mach number M*.

    Parameters
    ----------
        Ms : array_like
            Characteristic Mach number. If float, list, tuple is given as input, a conversion
            will be attempted. Must be 0 <= Ms <= sqrt((gamma + 1) / (gamma - 1))
        gamma : float
            Specific heats ratio. Default to 1.4
    
    Returns
    -------
        M : array_like
            Mach number
    """
    Ms_lim = np.sqrt((gamma + 1) / (gamma - 1))
    assert np.all(Ms >= 0) and np.all(Ms <= Ms_lim), "It must be 0 < Ms < {}".format(Ms_lim)
    assert isinstance(gamma, (float)) and gamma > 1, "The specific heat ratio must be > 1."
    return np.sqrt(2 / ((gamma + 1) / Ms**2 - (gamma - 1)))

def Stagnation_Temperature(T, u, cp):
    """
    Compute the stagnation temperature.

    cp * T + u**2 / 2 = cp * T0     (eq. 3.27)

    T0 is the temperature that would exist if the fluid element were brought to rest adiabatically.

    Parameters
    ----------
        T : array_like
            Static Temperature. If float, list, tuple is given as input, a conversion
            will be attempted. Must be T >= 0.
        u : array_like
            Velocity. If float, list, tuple is given as input, a conversion
            will be attempted.
        cp : float
            Specific heat at constant pressure. Must be cp > 0.
    
    Returns
    -------
        T0 : array_like
            Stagnation Temperature
    """
    T = np.asarray(T)
    u = np.asarray(u)
    assert np.all(T >= 0), "The static temperature must be >= 0."
    assert cp > 0, "The specific heat at constant pressure must be > 0."
    return T + u**2 / 2 / cp

def Pressure_Coefficient():
    raise NotImplementedError("Pressure_Coefficient function not yet implemented!")
    # Cp = (p - p_inf) / q_inf
    # q_inf = 0.5 * rho_inf * V_inf**2 = 0.5 * (gamma * p_inf) / (gamma * p_inf) * rho_inf * V_inf**2
    #         = 0.5 * gamma * p_inf * V_inf**2 / a_inf**2 = 0.5 * gamma * p_inf * M_inf**2
    # Cp = (p - p_inf) / (0.5 * gamma * p_inf * M_inf**2) = 
    #     = 2 / (gamma * M_inf**2) * (p / p_inf - 1)
    # pass

def Drag_Coefficient():
    raise NotImplementedError("Drag_Coefficient function not yet implemented!")
    # cd = D / (q_inf * S)
    # pass