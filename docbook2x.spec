%define oname  docbook2X

Summary:	A docbook to GNU Texinfo format converter
Name:		docbook2x
Version:	0.8.8
Release:	20
Group:		Publishing
License:	MIT
Url:		http://docbook2x.sourceforge.net/
Source0:	http://ovh.dl.sourceforge.net/sourceforge/%{name}/%{oname}-%{version}.tar.bz2
BuildRequires:	xsltproc
BuildRequires:	perl(XML::SAX)
Requires:	xsltproc

%description
Converts DocBook documents into the traditional Unix man page format
and the GNU Texinfo format.

%prep
%setup -qn %{oname}-%{version}

%build
# to avoid clashing with docbook2* from docbook-utils
%configure --program-transform-name='s/^docbook2/docbook2x-/'
%make

%install
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

