%define epoch	1

%define name	biopython
%define	version	1.51
%define	release	1

Summary:	The Biopython Project
Name:		%{name}
Version:	%{version}
Release:	%mkrel %{release}
Epoch:		%{epoch}
Source0:	http://biopython.org/files/%{name}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Url:		http://biopython.org/
Requires:	python-numpy
BuildRequires:	egenix-mx-base
BuildRequires:	python-reportlab, python-numpy, python-numpy-devel
BuildRequires:	gcc, epydoc, dos2unix
%py_requires -d

%package -n 	python-Bio
Summary: 	Python modules from the Biopython Project
Group:		Sciences/Biology
Requires:	python-numpy
Requires:	python-reportlab
Requires:	egenix-mx-base
Requires:	wise
Requires:	ncbi-blast
# don't explicitly require clustalw because it is non-free
Suggests:	clustalw
Provides:	biopython = %{epoch}:%{version}-%{release}
Obsoletes:	biopython

%package 	tools
Summary: 	Regression testing code and miscellaneous standalone scripts
Requires:	%{name} = %{epoch}:%{version}-%{release}
Suggests:	tkinter, wxPython
Group:		Sciences/Biology

%package -n	python-BioSQL
Summary:	Code for using Biopython with BioSQL databases
Requires:	%{name} = %{epoch}:%{version}-%{release}
Group:		Development/Python
Requires:	python-psycopg2
Requires:	python-mysql
Provides:	biopython-biosql = %{epoch}:%{version}-%{release}

%package	doc
Summary:	The Biopython Project documentation
Group:		Development/Python
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description
The Biopython Project is an international association of developers of
freely available Python tools for computational molecular biology.

http://biopython.org provides an online resource for modules,
scripts, and web links for developers of Python-based software for
life science research.

%description -n python-Bio
This package provides various Python modules from the Biopython Project 
used to process biological data.

%description tools
This package provides various scripts and tests that are comprised by the
Biopython Project.

%description -n python-BioSQL
BioSQL is meant to be a common data storage layer supported by all the
different Bio* projects, Bioperl, Biojava, Biopython, and Bioruby.
Entries stored through an application written in, say, Bioperl could
be retrieved by another written in Biojava.

%description doc
This package provides the documentation for the various components of the 
Biopython Project.

%prep
%setup -q

# remove Mac-related files
rm -f Tests/CodonUsage/.DS_Store
# remove CVS dirs
find -type d -name CVS | xargs rm -rf 
# convert wrong end of line
find -type f -exec dos2unix -b -U {} \;

%build
yes | python setup.py build

# build api
yes | epydoc -o api Bio BioSQL

%install
yes | python setup.py install --root=%{buildroot}

mkdir -p %{buildroot}/%_datadir/%{name}-%{version} 
cp -r Tests Scripts %{buildroot}/%_datadir/%{name}-%{version}

%clean
%__rm -rf %{buildroot}

%files -n python-Bio
%defattr(-,root,root,0755)
%py_platsitedir/Bio
%py_platsitedir/*.egg-info
%doc CONTRIB DEPRECATED LICENSE NEWS README

%files -n python-BioSQL
%defattr(-,root,root,0755)
%py_platsitedir/BioSQL
%doc LICENSE

%files tools
%defattr(-,root,root,0755)
%_datadir/%{name}-%{version}/Tests
%_datadir/%{name}-%{version}/Scripts

%files doc
%defattr(-,root,root,0755)
%doc Doc/*.pdf Doc/examples/
%doc api
