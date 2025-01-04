"""
Aquest codi inclou la classe amb el gradient substitut presentat a la memòria del treball,
seguint l'algoritme de la retropropagació.
"""


import torch
import math

class NewSurrogate(torch.autograd.Function):
    """
    Gradient substitut de la funció esglaó de Heaviside fent servir l'algoritme de retropropagació.

    **Pas endavant:** funció esglaó Heaviside.

        .. fórmula::

            S=\\begin{cases} 1 & \\text{if U ≥ U$_{\\rm thr}$} \\\\
            0 & \\text{if U < U$_{\\rm thr}$}
            \\end{cases}

    **Pas enrere:** Gradient de la funció sigmoide ràpida centrada en 1. És la proposta que es presenta en aquest TFM.

        .. fórmula::

                S&≈\\frac{U}{1 + k|U|} \\\\
                \\frac{∂S}{∂U}&=\\frac{1}{(1+k(|U|-1))^2}

    :math:`k` és per defecte 25, i es pot modificar cridant\
        ``new_surrogate(slope=25)``.
    """


    @staticmethod
    def forward(ctx, input_, slope=5):
        ctx.save_for_backward(input_)
        ctx.slope = slope
        out = (input_ > 0).float()
        return out

    @staticmethod
    def backward(ctx, grad_output):
        (input_,) = ctx.saved_tensors
        grad_input = grad_output.clone()
        grad = grad_input / (1 + torch.abs(ctx.slope * (input_ - 1.0)))** 2

        return grad, None


def new_surrogate(slope=25):
    """Gradient substitut proposat en aquest projecte parametritzat amb un pendent (paràmetre k)."""

    slope = slope
    def inner(x):
        return NewSurrogate.apply(x, slope)

    return inner

