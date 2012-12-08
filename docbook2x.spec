%define oname  docbook2X

Name:		docbook2x
Version:	0.8.8
Release:	9
Summary:	A docbook to GNU Texinfo format converter
Group:		Publishing
Url:		http://docbook2x.sourceforge.net/
License:	MIT
Source0:	http://ovh.dl.sourceforge.net/sourceforge/%{name}/%{oname}-%{version}.tar.bz2
BuildRequires:	libxslt-proc
BuildRequires:	perl(XML::SAX)
Requires:	xsltproc

%description
Converts DocBook documents into the traditional Unix man page format
and the GNU Texinfo format.

%prep
%setup -q -n %{oname}-%{version}

%build
# to avoid clashing with docbook2* from docbook-utils
%configure2_5x --program-transform-name='s/^docbook2/docbook2x-/'
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%{_bindir}/db2x_manxml
%{_bindir}/db2x_texixml
%{_bindir}/db2x_xsltproc
%{_bindir}/docbook2x-man
%{_bindir}/docbook2x-texi
%{_bindir}/sgml2xml-isoent
%{_bindir}/utf8trans
%{_docdir}/docbook2X
%{_datadir}/docbook2X
%{_mandir}/man1/*
%{_infodir}/*


%changelog
* Thu Jun 07 2012 Andrey Bondrov <abondrov@mandriva.org> 0.8.8-9
+ Revision: 803061
- Drop some legacy junk

* Fri Dec 31 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.8.8-8mdv2011.0
+ Revision: 626850
- change binaries renaming to match debian package

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.8.8-7mdv2011.0
+ Revision: 610261
- rebuild

* Mon Feb 01 2010 Emmanuel Andry <eandry@mandriva.org> 0.8.8-6mdv2010.1
+ Revision: 499218
- use program-transform-name to avoid conflict with docbook-utils

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 0.8.8-5mdv2010.0
+ Revision: 428308
- rebuild

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 0.8.8-4mdv2009.0
+ Revision: 266574
- rebuild early 2009.0 package (before pixel changes)

* Sun May 04 2008 Funda Wang <fwang@mandriva.org> 0.8.8-3mdv2009.0
+ Revision: 200861
- Should requires libxslt-proc

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - do not hardcode bz2 extension
    - info file must be unregistered before being uninstalled

* Thu May 10 2007 JÃ©rÃ´me Soyer <saispo@mandriva.org> 0.8.8-1mdv2008.0
+ Revision: 26057
- New release 0.8.8
- Import docbook2x



* Wed May 10 2006 Giuseppe Ghibò <ghibo@mandriva.org> 0.8.7-2mdk
- Added libxslt-proc to BuildRequires.

* Fri Apr 28 2006 Jerome Soyer <saispo@mandriva.org> 0.8.7-1mdk
- New release 0.8.7

* Mon Apr 24 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.8.6-2mdk
- Add BuildRequires

* Thu Apr 06 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.8.6-1mdk
- New release 0.8.6

* Thu Feb 16 2006 Austin Acton <austin@mandriva.org> 0.8.5-3mdk
- fix lib64 build
- tidy file list
- fix summary

* Tue Feb 14 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.8.5-2mdk
- Rebuild

* Thu Feb 14 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.8.5-1mdk 
- Fisrt Mandriva Release
