
# python source file for implementation of custom python/gdb api/functions routine

import gdb
import os

# each separate code section starts with and and by:
####    ####    ####    ####    ####    ####    ####    ####

####    ####    ####    ####    ####    ####    ####    ####
#    global color setup
GDB_PROMPT = ""
COLOR_FG_RED_BD = "\033[01;31m"
COLOR_CLS = "\033[0m"
####    ####    ####    ####    ####    ####    ####    ####

####    ####    ####    ####    ####    ####    ####    ####
#    print struct values recursively
# based on great advice:
#  http://stackoverflow.com/questions/16787289/gdb-python-parsing-structures-each-field-and-print-them-with-proper-value-if
# TODO: FIXME: char management
def is_container(v):
	c = v.type.code
	return (c == gdb.TYPE_CODE_STRUCT or c == gdb.TYPE_CODE_UNION)

def is_pointer(v):
	return (v.type.code == gdb.TYPE_CODE_PTR)

def print_struct(s, level_limit = -1, level = 0):
	
	if not is_container(s):
		gdb.write('%s %x\n' % (s.type, s))
		return
	
	if level >= level_limit:
		gdb.write('%s { ... },\n' % (s.type,))
		return
	
	indent = '\t' * level
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
			print_struct(v1, level_limit, level + 1)
		elif is_container(v):
			gdb.write('%s %s: ' % (indent, k))
			print_struct(v, level_limit, level + 1)
		else:
			gdb.write('%s %s: %s,\n' % (indent, k, v))
	gdb.write('%s},\n' % (indent,))


class PrintStruct(gdb.Command):
	
	
	'''Print structure displaying its elements of pointers recursively
print-struct [/LEVEL_LIMIT] STRUCT-VALUE

Location: python extension config file'''
	
	
	def __init__(self):
		super(PrintStruct, self).__init__('print-struct', gdb.COMMAND_DATA, gdb.COMPLETE_SYMBOL, False)
		
		
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
					raise gdb.GdbError(PrintStruct.__doc__)
				(expr, limit) = (arg[end:], limit)
		try:
			v = gdb.parse_and_eval(expr)
		except gdb.error, e:
			raise gdb.GdbError(e.message)
		print_struct(v, limit)


PrintStruct()
####    ####    ####    ####    ####    ####    ####    ####


####    ####    ####    ####    ####    ####    ####    ####
#    internal helper functions for getting gdb context information from runtime


def get_value(var = None, fmt = "", t = int):
	'''get python value from gdb variable'''
	if var is None:
		return t(0);
	try:
		svalue = gdb.execute("p%s %s" % (fmt, var), False, True)
		r = ( svalue[ svalue.rfind(" = ") + 2 : -1 ] )
		if var == "__LINE__":
			# workaround for "print __LINE__" gdb issue
			r = r.replace("0x", "")
		r = r.strip(" ")
		if var == "__func__" or var == "__FILE__":
			r = r.strip('"')
	except:
		pass
		r = 0
	return t(r)


def get_ctx_file(path = "full"):
	'''get string value with the path to the current context source file'''
	if not is_running():
		return ""
	r = get_value("__FILE__", "", str)
	if r == "0":
		r = ""
	if path != "full":
		r = os.path.basename(r)
	return r


def get_ctx_func():
	'''get string value with the function name in the current context'''
	r = get_value("__func__", "", str)
	if r == "0":
		r = ""
	return r


def get_ctx_line_s(n = None):
	'''get string value with the n-th source code line in the current context'''
	if n is None or n == 0:
		r = ""
	else:
		try:
			r = gdb.execute("list %s,%s" % (n, n), False, True)
		except:
			pass
			r = ""
	return r


def get_ctx_line_n():
	'''get python string value with the source code line number in the current context'''
	if is_running():
		r = get_value("__LINE__", "", str)
	else:
		r = ""
	return r


def get_ctx_line_n_define():
	svalue = gdb.execute("info macro __LINE__", False, True)
	try:
		r = (svalue[ svalue.rfind("#define __LINE__") : -1 ].split())[2]
	except:
		pass
		r = 0
	return r


def get_ctx_address():
	'''get string value with the instruction address in the current context'''
	if is_running():
		try:
			svalue = gdb.execute("x/i $pc", False, True)
			r = (svalue.split())[1]
		except:
			pass
			r = ""
	else:
		r = ""
	return r


def is_running():
	'''get application run status in the current context'''
	if get_ctx_func() == "":
		r = False
	else:
		r = True
	return r

def is_cgdb(var = None):
	'''get cgdb instance status'''
	# had to duplicate get_value() due to broken python support in CGDB
	if var is None:
		return False
	try:
		svalue = gdb.execute("p%s %s" % ("/d", var), False, True)
		r = ( svalue[ svalue.rfind(" = ") + 2 : -1 ] )
		r = r.strip(" ")
		r = r.strip('"')
		if r == "1":
			r = True
	except:
		pass
		r = False
	return r
####    ####    ####    ####    ####    ####    ####    ####


####    ####    ####    ####    ####    ####    ####    ####
#    user defined prompt experiments
# http://stackoverflow.com/questions/6103887/how-do-i-access-the-registers-with-python-in-gdb
# https://sourceware.org/gdb/onlinedocs/gdb/Prompt.html
# https://sourceware.org/gdb/onlinedocs/gdb/gdb_002eprompt.html#gdb_002eprompt
# https://sourceware.org/gdb/onlinedocs/gdb/Basic-Python.html
# http://www.cinsk.org/wiki/Debugging_with_GDB:_How_to_create_GDB_Commands_in_Python


def prompt_hook(prompt = None):
	'''custom prompt hook'''
	if is_cgdb("$USE_OPT_CGDB"):
		# terribly implement in CGDB
		return None
	global GDB_PROMPT
	global COLOR_FG_RED_BD
	global COLOR_CLS
	if GDB_PROMPT == "":
		GDB_PROMPT = prompt
	use_colors = get_value("$USE_OPT_COLORS", "/d")
	use_sprompt = get_value("$USE_OPT_SMARTPROMPT", "/d")
	if use_colors == 1:
		color_fg_red_bd = COLOR_FG_RED_BD
		color_cls = COLOR_CLS
	else:
		color_fg_red_bd = ""
		color_cls = ""
	if use_sprompt and is_running():
		# set a format string for custom smart prompt
		p = " %s | %s(): %s @ %s%s" % ( get_ctx_file("base"), get_ctx_func(), get_ctx_line_n(), get_ctx_address(), GDB_PROMPT)
	else:
		p = GDB_PROMPT
	return "%s%s%s" % (color_fg_red_bd, p, color_cls)

gdb.prompt_hook = prompt_hook
####    ####    ####    ####    ####    ####    ####    ####


