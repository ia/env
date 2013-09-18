
# python source file for implementation of custom python/gdb api/functions routine

import gdb

# each separate code section starts with and and by:
####    ####    ####    ####    ####    ####    ####    ####

####    ####    ####    ####    ####    ####    ####    ####
# print struct values recursively
# based on great advice:
#  http://stackoverflow.com/questions/16787289/gdb-python-parsing-structures-each-field-and-print-them-with-proper-value-if

def is_container(v):
    c = v.type.code
    return (c == gdb.TYPE_CODE_STRUCT or c == gdb.TYPE_CODE_UNION)

def is_pointer(v):
    return (v.type.code == gdb.TYPE_CODE_PTR)

def print_struct_follow_pointers(s, level_limit = 3, level = 0):
    indent = ' ' * level

    if not is_container(s):
        gdb.write('%s %x\n' % (s.type, s))
        return

    if level >= level_limit:
        gdb.write('%s { ... },\n' % (s.type,))
        return

    gdb.write('%s {\n' % (s.type,))
    for k in s.type.keys():
        v = s[k]
        if is_pointer(v):
            gdb.write('%s %s: %s' % (indent, k, v))
            try:
                v1 = v.dereference()
                v1.fetch_lazy()
            except gdb.error:
                gdb.write(',\n')
                continue
            else:
                gdb.write(' -> ')
            print_struct_follow_pointers(v1, level_limit, level + 1)
        elif is_container(v):
            gdb.write('%s %s: ' % (indent, k))
            print_struct_follow_pointers(v, level_limit, level + 1)
        else:
            gdb.write('%s %s: %s,\n' % (indent, k, v))
    gdb.write('%s},\n' % (indent,))

class PrintStructFollowPointers(gdb.Command):
    '''
    print-struct-follow-pointers [/LEVEL_LIMIT] STRUCT-VALUE
    '''
    def __init__(self): 
        super(PrintStructFollowPointers, self).__init__(
            'print-struct-follow-pointers',
            gdb.COMMAND_DATA, gdb.COMPLETE_SYMBOL, False)

    def invoke(self, arg, from_tty):
        s = arg.find('/')
        if s == -1:
            (expr, limit) = (arg, 3)
        else:
            if arg[:s].strip():
                (expr, limit) = (arg, 3)
            else:
                i = s + 1
                for (i, c) in enumerate(arg[s+1:], s + 1):
                    if not c.isdigit():
                        break
                end = i
                digits = arg[s+1:end]
                try:
                    limit = int(digits)
                except ValueError:
                    raise gdb.GdbError(PrintStructFollowPointers.__doc__)
                (expr, limit) = (arg[end:], limit)
        try:
            v = gdb.parse_and_eval(expr)
        except gdb.error, e:
            raise gdb.GdbError(e.message)

        print_struct_follow_pointers(v, limit)

PrintStructFollowPointers()
####    ####    ####    ####    ####    ####    ####    ####


####    ####    ####    ####    ####    ####    ####    ####
#    user defined prompt experiments
# http://stackoverflow.com/questions/6103887/how-do-i-access-the-registers-with-python-in-gdb
# https://sourceware.org/gdb/onlinedocs/gdb/Prompt.html
# https://sourceware.org/gdb/onlinedocs/gdb/gdb_002eprompt.html#gdb_002eprompt
# https://sourceware.org/gdb/onlinedocs/gdb/Basic-Python.html

# http://www.cinsk.org/wiki/Debugging_with_GDB:_How_to_create_GDB_Commands_in_Python

def custom_prompt(current_prompt = None):
    print "test"
    print current_prompt
#    value = ""
    value = gdb.execute("print $USE_OPT_COLORS", False, True)
#    print gdb.parameter("print $USE_OPT_COLORS")
#    print v[2]
#    sym, r = gdb.lookup_symbol("$USE_OPT_COLORS")
 #   print sym.Value
#    print gdb.selected_frame().read_var("$USE_OPT_COLORS")
    print "val = %s" % value[0]
    print "val = %s" % value[1]
    print "val = %s" % value[2]
    print "val = %s" % value[3]
    print "val = %s" % value[4]
    print "val = %s" % value[5]
    print "val = %s" % value[6]
    print ""
    return "\033[01;31m gdb.py>\033[0m "

gdb.prompt_hook = custom_prompt
####    ####    ####    ####    ####    ####    ####    ####

