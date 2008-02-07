Summary: The Biopython Project
Name: biopython
Version: 1.44
Release: %mkrel 1
Source0: http://biopython.org/files/%{name}-%{version}.tar.gz
License: BSD
Group: Development/Python
BuildRoot: %{_tmppath}/%{name}-buildroot
Url: http://www.biopython.org/
BuildRequires: python-devel
BuildRequires: python-numeric-devel python-numeric
BuildRequires: egenix-mx-base
BuildRequires: python-reportlab
BuildRequires: gcc
BuildRequires: epydoc
BuildRequires: dos2unix

%package -n python-Bio
Summary: The Biopython Project
Group: Sciences/Biology
Requires: python-numeric
Requires: python-reportlab
Requires: egenix-mx-base
Requires: python-Martel = %{version}
Provides: biopython = %{version}
Obsoletes: biopython

%package tools
Summary: Regression testing code and miscellaneous, possibly useful, standalone scripts
Requires: %{name} = %{version}
Group: Sciences/Biology

%package -n python-Martel
Summary: Biopython parser generator
Group: Development/Python
Provides: biopython-martel = %{version}
Obsoletes: biopython-martel

%package -n python-BioSQL
Summary: Code for using Biopython with BioSQL databases
Requires: %{name} = %{version}
Group: Development/Python
Requires: pyPgSQL
Requires: MySQL-python
Provides: biopython-biosql = %{version}
Obsoletes: biopython-biosql

%package doc
Summary: The Biopython Project documentation
Group: Development/Python
Requires: %{name} = %{version}

%description
     "The Biopython Project" - http://www.biopython.org/ is an
international association of developers of freely available Python
tools for computational molecular biology.

biopython.org provides an online resource for modules, scripts, and
web links for developers of Python-based software for life science
research.

%description -n python-Bio
     "The Biopython Project" - http://www.biopython.org/ is an
international association of developers of freely available Python
tools for computational molecular biology.

biopython.org provides an online resource for modules, scripts, and
web links for developers of Python-based software for life science
research.

%description tools
     "The Biopython Project" - http://www.biopython.org/ is an
international association of developers of freely available Python
tools for computational molecular biology.

%description -n python-Martel
Martel uses a modified form of the Perl regular expression language to 
describe the format of a file. The definition is used to generate a 
parser for that format. An input file is converted into a parse tree, 
which is traversed in prefix order to generate SAX 2.0 events, as used 
in XML processing. Element names and attributes are specified in the 
regular expression grammar using the named group extension popularized 
by Python. 

The events can be used by any SAX handler. Some of the common handlers 
can: build a DOM tree or any other data structures, load an XML database,
identify specific data fields (accession number, sequence, cross 
reference), find the record start and end positions, and drive an XSL 
transformation. 

%description -n python-BioSQL
BioSQL is meant to be a common data storage layer supported by all the
different Bio* projects, Bioperl, Biojava, Biopython, and Bioruby.
Entries stored through an application written in, say, Bioperl could
be retrieved by another written in Biojava.

%description doc
     "The Biopython Project" - http://www.biopython.org/ is an
international association of developers of freely available Python
tools for computational molecular biology.

biopython.org provides an online resource for modules, scripts, and
web links for developers of Python-based software for life science
research.


%prep
%setup -q

rm -f Tests/CodonUsage/.DS_Store
# remove CVS dirs
find -type d -name CVS | xargs rm -rf 
# convert wrong end of line
find -type f -exec dos2unix -U {} \;


%build
yes | python setup.py build

# build api
yes | epydoc -o api Bio Martel BioSQL


%install
yes | python setup.py install --root=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/%_datadir/%{name}-%{version} 
cp -r Tests Scripts $RPM_BUILD_ROOT/%_datadir/%{name}-%{version}



%clean
rm -rf $RPM_BUILD_ROOT

%files -n python-Bio
%defattr(-,root,root,0755)
%py_platsitedir/Bio
%py_platsitedir/*.5.egg-info
%doc CONTRIB LICENSE NEWS README


%files tools
%defattr(-,root,root,0755)
%_datadir/%{name}-%{version}/Tests
%_datadir/%{name}-%{version}/Scripts


%files -n python-Martel
%defattr(-,root,root,0755)
%py_platsitedir/Martel
%doc LICENSE


%files -n python-BioSQL
%defattr(-,root,root,0755)
%py_platsitedir/BioSQL
%doc LICENSE

%files doc
%defattr(-,root,root,0755)
%doc Doc/*
%doc api


