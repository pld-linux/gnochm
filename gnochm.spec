Summary:	A CHM file viewer for Gnome
Summary(pl.UTF-8):   Przeglądarka plików CHM dla Gnome
Name:		gnochm
Version:	0.9.8
Release:	2
License:	GPL v2+
Group:		Applications/Publishing
Source0:	http://dl.sourceforge.net/gnochm/%{name}-%{version}.tar.gz
# Source0-md5:	2451c736b133b93292991a701eb692ea
Patch0:		%{name}-desktop.patch
URL:		http://gnochm.sourceforge.net/
BuildRequires:	GConf2-devel
BuildRequires:	autoconf
BuildRequires:	automake
%pyrequires_eq	python
BuildRequires:	chmlib-devel
BuildRequires:	gettext-devel
BuildRequires:	libtool
BuildRequires:	python-devel >= 2.5
BuildRequires:	rpm-pythonprov 
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper
Requires(post,preun):	GConf2
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	scrollkeeper
Requires(post,postun):	shared-mime-info
Requires:	python-chm >= 0.8.3
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

%description -l pl.UTF-8
Przeglądarka plików CHM dla Gnome charakteryzująca się:
- Pełnym wyszukiwaniem tekstu
- Zakładkami
- Obsługą zewnętrznych powiązań ms-its
- Konfigurowalnym wsparciem dla powiązań HTTP
- Obsługą języków narodowych

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
update-mime-database %{_datadir}/mime ||:

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
