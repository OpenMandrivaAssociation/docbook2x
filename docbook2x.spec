%define oname  docbook2X

Name: 		docbook2x
Version: 	0.8.8
Release:	%mkrel 2
Group:		Publishing
Url:		http://docbook2x.sourceforge.net/
Summary:	A docbook to GNU Texinfo format converter
License:	MIT
BuildRoot:	%{_tmppath}/%name-%version-buildroot
Source0:	http://ovh.dl.sourceforge.net/sourceforge/%{name}/%{oname}-%{version}.tar.bz2
BuildRequires:	libxslt-proc
BuildRequires:	perl(XML::SAX)
Requires(post): info-install
Requires(preun):info-install
Conflicts:       docbook-utils

%description
Converts DocBook documents into the traditional Unix man page format
and the GNU Texinfo format.

%prep
%setup -q -n %{oname}-%{version}

%build

%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std

%post
%_install_info %name

%preun
%_remove_install_info %name

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root)
%{_bindir}/db2x_manxml
%{_bindir}/db2x_texixml
%{_bindir}/db2x_xsltproc
%{_bindir}/docbook2man
%{_bindir}/docbook2texi
%{_bindir}/sgml2xml-isoent
%{_bindir}/utf8trans
%{_docdir}/docbook2X
%{_datadir}/docbook2X
%{_mandir}/man1/*
%{_infodir}/*
