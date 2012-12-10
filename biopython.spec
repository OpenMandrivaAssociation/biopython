%define epoch	1

%define name	biopython
%define	version	1.58
%define	release	1

Summary:	The Biopython Project
Name:		%{name}
Version:	%{version}
Release:	%mkrel %{release}
Epoch:		%{epoch}
Source0:	http://biopython.org/files/%{name}-%{version}.tar.gz
Patch0:		lm-1.58.patch
License:	BSD
Group:		Development/Python
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Url:		http://biopython.org/
Requires:	python-numpy
BuildRequires:	egenix-mx-base
BuildRequires:	flex
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
%patch0 -p0

# remove Mac-related files
rm -f Tests/CodonUsage/.DS_Store
# remove CVS dirs
find -type d -name CVS | xargs rm -rf 
# convert wrong end of line
find -type f -exec dos2unix -b -U {} \;

%build
yes | PYTHONDONTWRITEBYTECODE= python setup.py build

# build api
export PYTHONPATH=`dir -d build/lib.*`
yes | epydoc -o api Bio BioSQL

%install
yes | PYTHONDONTWRITEBYTECODE= python setup.py install --root=%{buildroot}

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



%changelog
* Thu Aug 18 2011 Lev Givon <lev@mandriva.org> 1:1.58-1mdv2012.0
+ Revision: 695239
- Update to 1.58.

* Fri Nov 26 2010 Lev Givon <lev@mandriva.org> 1:1.56-1mdv2011.0
+ Revision: 601565
- Update to 1.56.

* Tue Nov 02 2010 Ahmad Samir <ahmadsamir@mandriva.org> 1:1.55-2mdv2011.0
+ Revision: 591933
- rebuild for python 2.7

* Mon Sep 13 2010 Lev Givon <lev@mandriva.org> 1:1.55-1mdv2011.0
+ Revision: 578020
- Update to 1.55.

* Wed Jul 14 2010 Lev Givon <lev@mandriva.org> 1:1.54-1mdv2011.0
+ Revision: 552994
- Update to 1.54.

* Wed Dec 16 2009 Lev Givon <lev@mandriva.org> 1:1.53-1mdv2010.1
+ Revision: 479515
- Update to 1.53.

* Wed Sep 23 2009 Lev Givon <lev@mandriva.org> 1:1.52-1mdv2010.0
+ Revision: 447573
- Update to 1.52.

* Mon Aug 17 2009 Lev Givon <lev@mandriva.org> 1:1.51-1mdv2010.0
+ Revision: 417346
- Update to 1.51.

* Tue Apr 21 2009 Lev Givon <lev@mandriva.org> 1:1.50-1mdv2010.0
+ Revision: 368591
- Update to 1.50.

* Thu Dec 25 2008 Funda Wang <fwang@mandriva.org> 1:1.49-4mdv2009.1
+ Revision: 318982
- fix file list
- rebuild for new python

* Fri Dec 19 2008 Lev Givon <lev@mandriva.org> 1:1.49-3mdv2009.1
+ Revision: 316314
- Fix python-BioSQL requirements.

* Fri Dec 12 2008 Lev Givon <lev@mandriva.org> 1:1.49-2mdv2009.1
+ Revision: 313641
- Fix provides/requires to include epoch.

* Tue Dec 02 2008 Lev Givon <lev@mandriva.org> 1:1.49-1mdv2009.1
+ Revision: 309262
- Update to 1.49.
  Update dependencies.

* Sun Nov 09 2008 Lev Givon <lev@mandriva.org> 1.49b-1mdv2009.1
+ Revision: 301624
- Update to 1.49b.

* Mon Sep 15 2008 Lev Givon <lev@mandriva.org> 1.47-2mdv2009.0
+ Revision: 284834
- Make doc fix really work.

* Mon Sep 08 2008 Lev Givon <lev@mandriva.org> 1.47-1mdv2009.0
+ Revision: 282429
- Fix busted Tutorial.pdf.
  Don't include doc making files.
- Update to 1.47.

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.44-3mdv2009.0
+ Revision: 243315
- rebuild

* Thu Feb 07 2008 Gaëtan Lehmann <glehmann@mandriva.org> 1.44-1mdv2008.1
+ Revision: 163691
- 1.44

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Aug 27 2007 Gaëtan Lehmann <glehmann@mandriva.org> 1.43-1mdv2008.0
+ Revision: 72168
- 1.43


* Wed Jan 31 2007 Nicolas Lécureuil <neoclust@mandriva.org> 1.42-2mdv2007.0
+ Revision: 115728
- Rebuild against new python
- Import biopython

* Fri Aug 11 2006 glehmann
+ 08/10/06 17:59:58 (55453)
update to 1.42

* Mon Jul 31 2006 glehmann
+ 07/30/06 09:51:44 (42642)
Import biopython

* Fri Jul 01 2005 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 1.40-0.20050420.3mdk
- rename packages

* Mon May 23 2005 Gaetan Lehmann <glehmann@n4.mandrakesoft.com> 1.40-0.20050420.2mdk
- add missing buildrequires

* Thu Apr 21 2005 Gaetan Lehmann <glehmann@n4.mandrakesoft.com> 1.40-0.20050420.1mdk
- cvs update
- use mkrel

* Fri Apr 01 2005 Gaetan Lehmann <glehmann@n4.mandrakesoft.com> 1.40-0.20050331.1mdk
- cvs update

* Sun Mar 20 2005 Gaetan Lehmann <glehmann@n4.mandrakesoft.com> 1.40-0.cvs20050320.1mdk
- cvs update

* Sun Mar 06 2005 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 1.40-0.cvs20050306.1mdk
- cvs update

* Tue Feb 22 2005 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 1.40-0.cvs20050222.1mdk
- cvs update

* Thu Feb 17 2005 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 1.40-0.cvs20050217.1mdk
- cvs update
- add build section
- fix some lint

* Tue Feb 15 2005 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 1.40-0.cvs20050215.1mdk
- 1.40 cvs

* Thu Feb 10 2005 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 1.30-3mdk 
- patch for python 2.4 (from freshports.org)
- fix path for python 2.4
- add api
- fix some lints

* Sat Oct 16 2004 Michael Scherer <misc@mandrake.org> 1.30-2mdk 
- fix Requires, #12092
- fix BuildRequires

* Wed Sep 01 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.30-1mdk
- from Gaetan Lehmann <glehmann@netcourrier.com> :
	- Create package from scratch for mandrake system

