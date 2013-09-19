
# internal global gdb variables for flexible config setup

# some external tools like cgdb is not friendly to term escape color codes
set $USE_OPT_COLORS           = 1
# force to use arm architecture
set $USE_OPT_ARCH_ARM         = 0
# force to use 64 bit architecture
set $USE_OPT_ARCH_64B         = 1

# enable config with custom generic gdb settings
set $USE_CONFIG_SETTINGS      = 1

# enable config with custom basic gdb hooks and functions; TODO: file:line > gdb prompt
set $USE_CONFIG_FUNCTIONS     = 1

# enable config with custom python/gdb helper routine
set $USE_CONFIG_PYTHON        = 1

# enable epic config from reverse.put.as
set $USE_CONFIG_REVERSEPUTAS  = 1

# enable config with custom aliases for gdb commands
set $USE_CONFIG_ALIASES       = 1

# initialization of modular gdb config files based on variables above; TODO: cgdb configs management, config.colors for color management
source ~/.gdb/config.init

