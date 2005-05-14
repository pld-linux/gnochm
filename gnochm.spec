Summary:	A CHM file viewer for Gnome
Summary(pl):	Przegl±darka plików CHM dla Gnome
Name:		gnochm
Version:	0.9.5
Release:	1
License:	GPL v2+
Group:		Applications/Publishing
Source0:	http://dl.sourceforge.net/gnochm/%{name}-%{version}.tar.gz
# Source0-md5:	3acf586f7dbaa971f57f6f93f24eb131
Patch0:		%{name}-desktop.patch
URL:		http://gnochm.sourceforge.net/
BuildRequires:	GConf2-devel
BuildRequires:	autoconf
BuildRequires:	automake
%pyrequires_eq	python
BuildRequires:	chmlib-devel
BuildRequires:	libtool
BuildRequires:	python-devel >= 2.2.1
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper
Requires(post,preun):	GConf2
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	scrollkeeper
Requires(post,postun):	shared-mime-info
Requires:	python-chm >= 0.8.1
Requires:	python-gnome
Requires:	python-gnome-gconf
Requires:	python-gnome-extras-gtkhtml >= 2.10.0
Requires:	python-gnome-ui
Requires:	python-gnome-vfs >= 2.10.0
Requires:	python-pygtk-glade
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
%patch0 -p1

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

rm -r $RPM_BUILD_ROOT%{_datadir}/{application-registry,mime-info}

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post 
%gconf_schema_install gnochm.schemas
%scrollkeeper_update_post
%update_desktop_database_post
umask 022
update-mime-database %{_datadir}/mime

%preun
%gconf_schema_uninstall gnochm.schemas

%postun
%scrollkeeper_update_postun
%update_desktop_database_postun
if [ $1 = 0 ]; then
	umask 022
	update-mime-database %{_datadir}/mime
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ABOUT-NLS AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gnochm
%{_datadir}/%{name}
%{_datadir}/omf/gnochm
%{_pixmapsdir}/*
%{_desktopdir}/gnochm.desktop
%{_datadir}/mime/packages/gnochm.*
%{_mandir}/man1/*
%lang(it) %{_mandir}/it/man1/*
%{_sysconfdir}/gconf/schemas/gnochm.schemas
