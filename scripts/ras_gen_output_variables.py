"""
Routine to generate constants and description programmatically
"""
import textwrap

from pyras.controllers import RAS500


def __gen_var_names_description():
    """ """

    with RAS500() as rc:
        res = rc.Output_Variables()

    n_variables = res[0]
    descriptions = res[2]
    var_names = []

    for i in range(n_variables):
        name = res[1][i]
        var_name = name.upper().replace(' ', '_')
        var_name = var_name.replace('.', '')
        var_name = var_name.replace('#', 'N')
        var_name = var_name.replace('&_', '')
        var_name = var_name.replace('/', '_')
        var_names.append(var_name)

    return var_names, descriptions


def gen_var_docs():
    """ """
    digits = 3  # Max length of available IDs... currently go until 268
    var_names, descriptions = __gen_var_names_description()
    var_name_l = max([len(var) for var in var_names])

    for i in range(len(var_names)):
        desc = descriptions[i]
        l = len(var_names[i])
        l_id = digits - len(str(i))
        base = "  " + var_names[i] + (var_name_l - l)*' ' + ' '*(l_id + 1) + \
            str(i+1) + '  '
        base_len = len(base)
        line = textwrap.wrap(base + desc, 79)
        if len(line) == 1:
            line = ''.join(line)
        else:
            parts = []
            for l in line:
                parts.append(l)
                if l != line[-1]:
                    parts.append('\n' + ' '*base_len)
            line = ''.join(parts)
        print(line)


def gen_constants():
    """ """
    template = '{0} = {1}'
    var_names, descriptions = __gen_var_names_description()

    for i in range(len(var_names)):
        line = template.format(var_names[i], str(i+1))
        print(line)


if __name__ == '__main__':
    gen_constants()
    gen_var_docs()
