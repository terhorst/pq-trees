%{
#define SWIG_FILE_WITH_INIT
#include "../pqtree.h"
%}

%include "typemaps.i"
%include "std_set.i"
%include "std_string.i"
%include "std_list.i"

namespace std {
    %template(IntSet) set<int>;
    %template(IntList) list<int>;
    %template(IntSetList) list< set<int> >;
}

%module pqtree
%include "../pqtree.h"
%extend PQTree {
    string __repr__() { return $self->Print(); }
}
