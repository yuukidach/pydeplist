import sys
import distutils.core as discore

def setup_load (script_name, script_args=None, stop_after="run", **kwargs):
    """This is mainly from distutils.core.run_setup()
    Because it not support us to configurate the global variable for
    `exec()', I create a new function which is similiar to it but 
    can input global variables
    """
    if stop_after not in ('init', 'config', 'commandline', 'run'):
        raise ValueError("invalid value for 'stop_after': %r" % (stop_after,))

    discore._setup_stop_after = stop_after

    save_argv = sys.argv.copy()
    g = {'__file__': script_name}
    for key, val in kwargs.items():
        g[key] = val
    try:
        try:
            sys.argv[0] = script_name
            if script_args is not None:
                sys.argv[1:] = script_args
            # with open(script_name, 'rb') as f:
            f = open(script_name, 'rb')    
            exec(f.read(), g)
            f.close()
        finally:
            sys.argv = save_argv
            _setup_stop_after = None
    except SystemExit:
        # Hmm, should we do something if exiting with a non-zero code
        # (ie. error)?
        pass

    if discore._setup_distribution is None:
        raise RuntimeError(("'distutils.core.setup()' was never called -- "
               "perhaps '%s' is not a Distutils setup script?") % \
              script_name)

    # I wonder if the setup script's namespace -- g and l -- would be of
    # any interest to callers?
    #print "discore._setup_distribution:", discore._setup_distribution
    return discore._setup_distribution