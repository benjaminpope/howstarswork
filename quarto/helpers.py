from IPython.display import Markdown

def md_float(f):
    float_str = "{0:.2g}".format(f)
    if "e" in float_str:
        base, exponent = float_str.split("e")
        return Markdown(r"${0} \times 10^{{{1}}}$".format(base, int(exponent)))
    else:
        return float_str