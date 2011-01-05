from distutils.core import setup, Extension

pqtree_module = Extension('_pqtree',
                           sources=['pqtree.i', '../pqnode.cc', '../pqtree.cc'],
                           )

setup (name = 'pqtree',
       version = '0.1',
       author      = "Jonathan Terhorst",
       description = """Simple swig example from docs""",
       ext_modules = [pqtree_module],
       options={'build_ext':{'swig_opts':'-c++'}},
       py_modules = ["pqtree"],
       )

