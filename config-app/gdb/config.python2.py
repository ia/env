
# python 2.x source file for implementation of custom python/gdb api/functions routine

import gdb
import sys
import os
import string
import time
import argparse

# each separate code section starts with and and by:
####    ####    ####    ####    ####    ####    ####    ####

####    ####    ####    ####    ####    ####    ####    ####
#    global color setup
GDB_PROMPT   = ""
COLOR_RED    = "\033[31m"
COLOR_RED_BD = "\033[01;31m"
COLOR_CLS    = "\033[0m"
####    ####    ####    ####    ####    ####    ####    ####

####    ####    ####    ####    ####    ####    ####    ####
#    print struct values recursively
# based on great advice:
#  http://stackoverflow.com/questions/16787289/gdb-python-parsing-structures-each-field-and-print-them-with-proper-value-if
# TODO: FIXME: char management


def is_smart_radix():
	if is_opt("$USE_OPT_SMARTRADIX"):
		r = True
	else:
		r = False
	return r


def set_radix(v):
	try:
		gdb.execute("set radix %s" % v, False, False)
	except:
		pass
		return


def is_container(v):
	c = v.type.code
	return (c == gdb.TYPE_CODE_STRUCT or c == gdb.TYPE_CODE_UNION)


def is_pointer(v):
	return (v.type.code == gdb.TYPE_CODE_PTR)


def is_char(v):
	return (str(v.type) == "char")


def get_typevalue(v):
	if not is_smart_radix():
		return ""
	c = v.type.code
	if ((str(v.type) == "char") or (c == gdb.TYPE_CODE_CHAR)):
		svalue = str(unichr(v))
		printset = set(string.printable)
		isprintable = set(svalue).issubset(printset)
		if isprintable:
			return " // ['%s']" % svalue
	elif c == gdb.TYPE_CODE_INT:
		return " // [%d]" % int(v)
	elif c == gdb.TYPE_CODE_BOOL:
		if bool(v):
			return " // [T]"
		else:
			return " // [F]"
	elif c == gdb.TYPE_CODE_FLT:
		return " // [%f]" % float(v)
	return ""


def print_struct(s, level_limit = -1, level = 1):
	if not is_container(s):
		gdb.write('%s %x\n' % (s.type, s))
		return
	if level >= level_limit:
		gdb.write('%s {...},\n' % (s.type,))
		return
	indent = '\t' * level
	if level > 1:
		gdb.write(' {\n')
	else:
		gdb.write('struct %s {\n' % s.type)
	for k in s.type.keys():
		v = s[k]
		if is_pointer(v):
			gdb.write('%s%s%s = %s;' % (indent, v.type, k, v))
			try:
				v1 = v.dereference()
				v1.fetch_lazy()
			except gdb.error:
				gdb.write('\n')
				continue
			if not is_char(v1):
				print_struct(v1, level_limit, level + 1)
			else:
				gdb.write('\n')
		elif is_container(v):
			gdb.write('%s %s: ' % (indent, k))
			print_struct(v, level_limit, level + 1)
		else:
			gdb.write('%s%s %s = %s;%s\n' % (indent, v.type, k, v, get_typevalue(v)))
	gdb.write('%s};\n' % (indent.replace('\t','', 1)))


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
				for (i, c) in enumerate(arg[s + 1:], s + 1):
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
		if not is_smart_radix():
			set_radix("10.")
		print_struct(v, limit)
		if not is_smart_radix():
			set_radix("0x10")


PrintStruct()
####    ####    ####    ####    ####    ####    ####    ####


####    ####    ####    ####    ####    ####    ####    ####
class PrintMacro(gdb.Command):
	
	
	'''Print macro information
print-macro macro

Location: python extension config file'''
	
	
	def __init__(self):
		super(PrintMacro, self).__init__('print-macro', gdb.COMMAND_DATA, gdb.COMPLETE_SYMBOL, False)
	
	
	def invoke(self, arg, from_tty):
		try:
			svalue = gdb.execute("info macro %s" % arg, False, True)
		except:
			pass
			return
		input_clean = svalue.replace("Defined at ", "")
		# gdb.execute won't tell about macro existence, so check using its output
		if svalue == input_clean:
			return
		define_index = input_clean.rfind("\n#define")
		define_line = input_clean[define_index+1::].replace("\n", "\\n")
		prefix_line = input_clean[0:define_index]
		input_words = input_clean.split("\n")
		define_file = input_words[0]
		includes = input_words[1:-1]
		includes.reverse()
		l = len(includes)
		for e in range(l):
			includes[e] = includes[e].replace("  included at ", "")
		for e in range(1, l):
			print "%s%s" % ('\t' * (e - 1), includes[e])
		print "%s%s" % ('\t' * e, define_file)
		print "%s%s" % ('\t' * (e + 1), define_line.rstrip("\\n"))


PrintMacro()
####    ####    ####    ####    ####    ####    ####    ####


####    ####    ####    ####    ####    ####    ####    ####
#    internal helper functions for getting gdb context information from runtime


def get_value(var = None, fmt = ""):
	'''get python value from gdb variable'''
	if var is None:
		return ""
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
		r = ""
	return r


def get_ctx_location():
	try:
		svalue = gdb.execute("backtrace", False, True)
		loc_line = svalue.split("\n")
		loc = loc_line[0].split()
		return loc[-1], loc[1]
	except:
		pass
		r = ""
		return r, r


def get_ctx_file(path = "full"):
	'''get string value with the path to the current context source file'''
	if not is_running():
		return ""
	r = get_value("__FILE__")
	if r != "":
		if path != "full":
			r = os.path.basename(r)
	return r


def get_ctx_func():
	'''get string value with the function name in the current context'''
	r1, f = get_ctx_location()
	return f
	#return get_value("__func__")


def get_ctx_line_s(n = 0):
	'''get string value with the n-th source code line in the current context'''
	if n is None or n == 0:
		r = ""
	else:
		try:
			r = gdb.execute("list %s,%s" % (str(n), str(n)), False, True)
		except:
			pass
			r = ""
	return r


def get_ctx_line_n():
	'''get python string value with the source code line number in the current context'''
	if is_running():
		r = get_value("__LINE__")
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
	try:
		svalue = gdb.execute("x/i $pc", False, True)
		r = (svalue.split())[1]
	except:
		pass
		r = ""
	return r


def is_running():
	'''get application run status in the current context'''
	if get_ctx_address() == "":
		r = False
	else:
		r = True
	return r


def is_opt(var = None):
	'''get cgdb instance status'''
	# had to duplicate get_value() due to crappy python support in CGDB
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
class PrintTrace(gdb.Command):
	
	
	'''Print trace information
print-trace

Location: python extension config file'''
	
	
	def __init__(self):
		super(PrintTrace, self).__init__('print-trace', gdb.COMMAND_DATA, gdb.COMPLETE_SYMBOL, False)
	
	
	def invoke(self, arg, from_tty):
		print get_ctx_file('') + ":", get_ctx_func() + "():", get_ctx_line_s(get_ctx_line_n())


PrintTrace()
####    ####    ####    ####    ####    ####    ####    ####


####    ####    ####    ####    ####    ####    ####    ####
class RunTraceHelper(gdb.Command):
	
	
	'''Run application in trace mode from external script
run-trace-helper

Location: python extension config file'''
	
	# TODO: FIXME: arg, error output, clean code, routine: get line/function/file properly
	def __init__(self):
		super(RunTraceHelper, self).__init__('run-trace-helper', gdb.COMMAND_DATA, gdb.COMPLETE_SYMBOL, False)
	
	def trace(self, f, stack, n = 0):
	#	print "1"
		if ((stack is not None) and (stack != get_ctx_func())):
#			print "2"
	#		f.write(stack + "()" + " ====>>>> " + get_ctx_func() + "()\n")
			f.write(get_ctx_func() + "()" + " <<<<==== " + stack + "()\n")
#			trace_line = stack + " <<<<>>>> " + get_ctx_file('') + ":" + get_ctx_func() + "():" + get_ctx_line_s(int(get_ctx_line_n()) - n)
#		else:
#		print "3"
		trace_line = " ====>>>> " + get_ctx_file('') + ":" + get_ctx_func() + "():" + get_ctx_line_s(int(int(get_ctx_line_n()) - int(n)))
#		print "4"
	#	trace_line = " ====>>>> " + get_ctx_file('') + ":" + get_ctx_func() + "():"
#		print trace_line
		f.write(trace_line)
		#f.write(get_ctx_file('') + ":", get_ctx_func() + "():", get_ctx_line_s(get_ctx_line_n()))
		f.flush()
		
	def invoke(self, arg, from_tty):
		print "ARGARG:", arg.strip('"')
#		a_app = arg.split()[0]
#		print "a_app: ", a_app
	#	print "app: ", arg.find('--')
	#	print "args: ", arg[1:arg.find('--')]
	#	print "appargs: ", arg[arg.find('--')+2:-1]
#		print "app_bin: ", arg[arg.find('--')+2:-1].split()[0]
		
		my_args = arg[1:arg.find('--')]
		app_bin = arg[arg.find('--')+2:-1].split()[0]
		app_args = ' '.join(arg[arg.find('--')+2:-1].split()[1:])
		print "my_args: ", my_args
		print "app_bin: ", app_bin
		print "app_args: ", app_args
	#	print "10"
#		print sys.argv
#		print "20"
	#	self.argv = my_args
#		print "app_args: ", arg[arg.split().find(app_bin):-1]
	#	sys.exit(1)
		#print os.path.expanduser("~") + "/.gdb/log.trace"
	#	print 1
		parser = argparse.ArgumentParser(description='process run-trace-helper options')
	#	print 2
		parser.add_argument('-f', '--file',
				dest = 'filename',
				metavar='FILE',
				default = "/dev/stdout",
				type = str,
				help = "write trace to FILE (stdout by default)")
		
		parser.add_argument("-s", "--sleep",
				dest = "sleep",
				metavar = "INT",
				default = 0,
				type = float,
				help = "sleep timeout between traces (0 by default)")
		
		parser.add_argument('-d', '--directory',
				dest = 'srcdir',
				metavar='DIRECTORY',
				default = None,
				type = str,
				help = "directory with sources")
		
		parser.add_argument('-v', '--verbose',
				dest = 'verbose',
#				metavar='BOOL',
				default = False,
				action = "store_true",
#				type = bool,
				help = "print verbose information")
		args = parser.parse_args(my_args.split())
		
	#	print "arg:", arg
		if args.filename is not None and args.filename != "":
			fname = args.filename
			self.is_flush = False
		else:
			fname = "/dev/stdout"
			self.is_flush = True
		if args.verbose is not None and args.verbose == True:
			print "Using file for saving trace log:", fname
			print "Using sleep timeout:", args.sleep
			print "Using src/ directory:", args.srcdir
		if args.srcdir is not None and args.srcdir != "":
			try:
				print gdb.execute("directory " + args.srcdir, False, True)
			except:
				print "ERROR: GDB: python: run-trace-helper: directory " + args.srcdir
				return
		try:
			print gdb.execute("break main", False, True)
		except:
			print "ERROR: GDB: python: run-trace-helper: break main"
			return
		try:
			print gdb.execute("run " + app_args, False, True)
		except:
			print "ERROR: GDB: python: run-trace-helper: run", app_bin
			return
		try:
#			l = open(os.path.expanduser("~") + "/.gdb/log.trace", "w+")
#			l = open("/dev/stdout", "w+")
			l = open(fname, "w+")
		except:
			print "ERROR: GDB: python: run-trace-helper: can't open trace file for writing log:", fname
			return
		self.trace(l, None, 1)
#		stack = get_ctx_func()
		self.trace(l, None)
		stack = ""
		while is_running():
#			self.trace(l)
			try:
				stack = get_ctx_func()
				gdb.execute("step", False, True)
				#print gdb.execute("step", False, True)
				self.trace(l, stack)
				if args.sleep is not None and args.sleep != 0:
					time.sleep(args.sleep)
			except:
				pass
		l.close()


RunTraceHelper()
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
	global GDB_PROMPT
	global COLOR_RED
	global COLOR_RED_BD
	global COLOR_CLS
	if GDB_PROMPT == "":
		GDB_PROMPT = prompt
	use_colors = get_value("$USE_OPT_COLORS", "/d")
	use_sprompt = get_value("$USE_OPT_SMARTPROMPT", "/d")
	if use_colors and not is_opt("$USE_OPT_CGDB"):
		color_red_bd = COLOR_RED_BD
		color_cls = COLOR_CLS
	else:
		color_red_bd = ""
		color_cls = ""
	if use_sprompt and is_running():
		# set a format string for custom smart prompt
		if is_opt("$USE_OPT_CGDB"):
			p = " @ %s%s" % ( get_ctx_address(), GDB_PROMPT)
		else:
			file_line, function = get_ctx_location()
			p = " %s | %s() @ %s%s" % ( file_line, function, get_ctx_address(), GDB_PROMPT)
		# line won't work with old gcc versions:
		#  p = " %s | %s(): %s @ %s%s" % ( get_ctx_file("base"), get_ctx_func(), get_ctx_line_n(), get_ctx_address(), GDB_PROMPT)
	else:
		p = GDB_PROMPT
	return "%s%s%s" % (color_red_bd, p, color_cls)

gdb.prompt_hook = prompt_hook
####    ####    ####    ####    ####    ####    ####    ####


