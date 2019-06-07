"""
The fake vw that is actually using BXR
need BXR location and prior file in the environment var

Not going to support a lot of vw command line arguments. 
"""
import os
import sys
import argparse
import subprocess

from vwbxr import Model_bxr2vw, X_vw2bxr

__BXR_path = os.environ['BXRtrain'] if 'BXRtrain' in os.environ else None
__BXR_prior = os.environ['BXR_prior'] if 'BXR_prior' in os.environ else None

def parseargs():
    """
        p = subprocess.run(['vw', '-c', '--loss_function=logistic', '--noconstant', '--passes=1',
                                    '-l', '2', '-b', '25',
                                    '-d', str( cpath / (feature_fn) ),
                                    '-f', str( opath / (name + "_model.vw") ),
                                    '--readable_model', str( opath / (name + "_coef.vw") ) ], 
                            stderr = subprocess.PIPE, stdout = subprocess.PIPE)
    """

    parser = argparse.ArgumentParser(description="BXR Wrapper with Vowpal Wabbit interface -- FakeVW. \n"
                                                 "Please but BXRtrain binary in environment variable using name `BXRtrain` "
                                                 "and put the BXR prior file(if used) in variable `BXR_prior`.")

    # vw options
    parser.add_argument("-d", "--data", type=str, help="Training data file in VW format.")

    parser.add_argument("-c", "--cache", action="store_true", help="Save the cached BXR format file")
    parser.add_argument("--cache_file", type=str, default="", help="File name for the cached BXR format file. "
                                                                   "Default using <DATA>.bxrcache.")
    parser.add_argument("-k", "--kill_cache", action="store_true", help="Always create new cached file.")

    parser.add_argument("--loss_function", type=str, default="logistic", help="Tyle of loss function, ALWAYS IGNORED.") # ignore
    parser.add_argument("--passes", type=int, default=1, help="Number of passes over training data, ALWAYS IGNORED.") # ignore

    parser.add_argument("--noconstant", action="store_true", help="Fitting intercept, ALWAYS IGNORED.") # ignore

    parser.add_argument("-l", "--learning_rate", type=float, default=0.5, help="Learning rate, ALWAYS IGNORED.")
    parser.add_argument("--l1", type=float, default=0.0, help="Variance when using L1. Using L1 when value is non-zero.")
    parser.add_argument("--l2", type=float, default=0.0, help="Variance when using L2. Using L2 when value is non-zero.")

    parser.add_argument("-b", "--bit_precision", type=int, default=25, help="Bit precision, ALWAYS IGNORED.") # ignore

    parser.add_argument("-f", "--final_regressor", type=str, default="", help="ALWAYS IGNORED.") # ignore

    parser.add_argument("--readable_model", type=str, required=True, help="File name for the final readable model. "
                                                                          "Always use this argument for model destination")

    # for fake vw
    parser.add_argument("--keep_bxrmodel", action="store_true", help="Keep the original model output from BXR.")
    parser.add_argument("--show_bxr_stdout", action="store_true", help="Show BXR stdout to console.")

    parser.add_argument("--verbose", action="store_true", help="Verbose output")

    ret = parser.parse_args()
    if ret.cache_file == "":
        ret.cache_file = ret.data + ".bxrcache"
    return ret
    # return parser

def main():
    print("=== Running Fake VW --> actually BXR ===\n")

    args = parseargs()
    if __BXR_path is None:
        raise EnvironmentError("Require path to BXRtrain to be set in the environment.")

    comment = print if args.verbose else lambda *x: None

    bxr_args = ["-e", "0.001"] # set it same as the default value for reminder 

    if args.l1 == 0 and args.l2 > 0:
        bxr_args += ["-p", "2", "-V", str(args.l2)]
    elif args.l1 > 0 and args.l2 == 0:
        bxr_args += ["-p", "1", "-V", str(args.l1)]
    elif args.l1 == 0 and args.l2 == 0:
        bxr_args += ["-p", "2", "-V", "1.0"]
    else:
        raise ValueError("Does not support elasticnet -- setting both L1 and L2 penalty.")
    
    if __BXR_prior is not None:
        comment("using prior file", __BXR_prior)
        bxr_args += ["-I", __BXR_prior]
    

    if args.data == "":
        training_file = X_vw2bxr( sys.stdin, out="file" ).name
    else:
        training_file = args.cache_file
        if not os.path.exists( args.cache_file ) or args.kill_cache:
            tf = X_vw2bxr( open( args.data ), out=args.cache_file )
            tf.flush()
            tf.close()
        else:
            comment("using cached file", training_file)
    
    bxr_model_fn = args.readable_model + ".bxrmodel"

    # add training file and output model arguments
    bxr_args += [ training_file, bxr_model_fn ]

    if args.show_bxr_stdout:
        comment("piping BXR stdout to stdout")
        bxr_stdout = sys.stdout
    else:
        comment("hiding BXR stdout")
        bxr_stdout = subprocess.DEVNULL
    
    print("calling BXR training:")
    print( __BXR_path, " ".join(bxr_args) )

    # calling
    p = subprocess.run([ __BXR_path, *bxr_args ], 
                       stdout = bxr_stdout, stderr=sys.stderr)
    
    comment("converting BXR model file")
    Model_bxr2vw( open( bxr_model_fn ), open( args.readable_model, "w+" ) )

    print("Done")

    # post processing
    if not args.cache:
        comment("remove cache file")
        os.remove( args.cache_file )
    if not args.keep_bxrmodel:
        comment("remove BXR model file")
        os.remove( bxr_model_fn )

if __name__ == "__main__":
    main()