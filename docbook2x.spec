%define oname  docbook2X

Name: 		docbook2x
Version: 	0.8.8
Release:	%mkrel 8
Summary:	A docbook to GNU Texinfo format converter
Group:		Publishing
Url:		http://docbook2x.sourceforge.net/
License:	MIT
Source0:	http://ovh.dl.sourceforge.net/sourceforge/%{name}/%{oname}-%{version}.tar.bz2
BuildRequires:	libxslt-proc
BuildRequires:	perl(XML::SAX)
Requires:	xsltproc
Requires(post): info-install
Requires(preun):info-install
BuildRoot:	%{_tmppath}/%name-%version

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

%post
%_install_info %name

%preun
%_remove_install_info %name

%clean
rm -rf %{buildroot}

%files
%defattr (-,root,root)
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
