Summary:	A CHM file viewer for Gnome
Summary(pl):	Przegl±darka plików CHM dla Gnome
Name:		gnochm
Version:	0.9.2
Release:	1
License:	GPL
Group:		Applications/Publishing
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	f5476c21943ad669c62d860cd712487a
URL:		http://gnochm.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
%pyrequires_eq	python
BuildRequires:	chmlib-devel
BuildRequires:	python-devel >= 2.2.1
BuildRequires:	rpm-pythonprov
Requires(post):	%{_bindir}/gconftool-2
Requires(post):	scrollkeeper
Requires(postun):	scrollkeeper
Requires:	python-chm >= 0.8.0
Requires:	python-gnome
Requires:	python-gnome-gconf
Requires:	python-gnome-gtkhtml >= 2.0
Requires:	python-gnome-ui
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A CHM file viewer for Gnome. Features are:
- Full text search
- Bookmarks
- Support for external ms-its links
- Configurable support for HTTP links
- Internationalisation

%description -l pl
Przegl±darka plików CHM dla Gnome charakteryzuj±ca siê:
- Pe³nym wyszukiwaniem tekstu
- Zak³adkami
- Obs³ug± zewnêtrznych powi±zañ ms-its
- Konfigurowalnym wsparciem dla powi±zañ HTTP
- Obs³ug± jêzyków narodowych

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 \
	SHAREDMIME_TOOL=no

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post 
%{_bindir}/scrollkeeper-update
%gconf_schema_install

%postun -p %{_bindir}/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ABOUT-NLS AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gnochm
%{_datadir}/%{name}
%{_datadir}/omf/gnochm
%{_pixmapsdir}/*
%{_datadir}/applications/gnochm.desktop
%{_datadir}/mime-info/gnochm.*
%{_datadir}/mime/packages/gnochm.*
%{_datadir}/application-registry/gnochm.*
%{_mandir}/man?/*
%{_sysconfdir}/gconf/schemas/gnochm.schemas
