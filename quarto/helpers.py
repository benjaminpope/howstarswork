from IPython.display import Markdown

def md_float(f, digits=2):
    float_str = "{0:.{1}g}".format(f, digits)
    if "e" in float_str:
        base, exponent = float_str.split("e")
        return Markdown(r"${0} \times 10^{{{1}}}$".format(base, int(exponent)))
    else:
        return Markdown(float_str)