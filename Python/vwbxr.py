# script to convert vw format to bxr 
import io
import tempfile

_vw_model_header = """Version BXR.eugene.fakevw.0.0.1
Id
Min label:
Max label:
bits:
lda:0
0 ngram:
0 skip:
options: 
Checksum:
"""

def _feat_modify(f, mul=1.0):
    if mul == 1.0: return f
    if ":" not in f:  return f + ":" + str(mul)
    f = f.split(":")
    return f[0] + ":" + str( float(f[1]) * mul )

def vec_vw2bxr(vwstr):    
    vwstr = vwstr.replace("\n", "").split("|")
    label = vwstr[0].split(" ")[0]
    nsps = [ n.split(" ") for n in vwstr[1:] ]
    feats = []
    for n in nsps:
        nsmul = 1.0
        if n[0] != "" and ":" in n[0]: # exits namespace
            nsmul = float(n[0].split(":")[1])
        feats += [ _feat_modify(f, nsmul)  for f in n[1:] if f != "" ]
    
    return label + " " + " ".join( feats ) + "\n"

def vec_bxr2vw(bxrstr):
    # TODO
    pass

def X_vw2bxr( inp, out=None ):
    """
        inp: accept stream or actual text
        out: the kind of output format
            - "file": return a tempfile
            - "text": return text
            - "stream": return a io.StringIO instance
            - other string: output to this file
            - other io.TextIOBase instance: write to it
            - None: the kind of format from the inp
    """
    inpformat = None
    if isinstance( inp, io.TextIOBase ):
        inpformat = "stream"
    elif isinstance( inp, str ):
        inpformat = "text"
        inp = io.StringIO( inp )
    else:
        raise TypeError("Input should be either string or stream(instance of io.TextIOBase), but get %s"%inp.__class__.__name__)

    out = out or inpformat

    if out == "file":
        outstream = tempfile.NamedTemporaryFile("w+")
    elif out == "text" or out == "strem":
        outstream = io.StringIO()
    elif isinstance( out, str ):
        outstream = open(out, "w+") # will overwrite the file
    elif isinstance( out, io.TextIOBase ):
        outstream = out
    
    for l in inp:
        outstream.write( vec_vw2bxr(l) )
    outstream.seek(0) # move back to the beginning for reading

    return outstream.read() if out == "text" else outstream


def Model_bxr2vw( inp, out=None ):
    """
        inp: IO stream
        out: IO stream, if None, return a io.StringIO
    """
    if not isinstance( inp, io.TextIOBase ):
        raise TypeError("Input should be either string or stream(instance of io.TextIOBase), but get %s"%inp.__class__.__name__)

    if out is None: 
        out = io.StringIO()
    elif not isinstance( out, io.TextIOBase ):
        raise TypeError("Output should be either string or stream(instance of io.TextIOBase), but get %s"%out.__class__.__name__)
    
    # hard-coded to find weights where class = 1
    
    bxrmodel = inp.read().split("\n")
    out.write( _vw_model_header )
    for l in bxrmodel[3:]:
        l = l.split(" ")
        if l[1] == "1":
            out.write( "\n".join( l[2:] ) )
            return out