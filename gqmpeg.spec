Summary:	mpeg player frontend to mpg123
Summary(pl):	Nak³adka graficzna dla odtwarzacza mpg123
Name:		gqmpeg
Version:	0.8.3
Release:	1
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	ftp://download.sourceforge.net/pub/sourceforge/gqmpeg/%{name}-%{version}.tar.gz
Patch0:		%{name}-desktop.patch
Icon:		gqmpeg.xpm
URL:		http://gqmpeg.sourceforge.net/
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	imlib-devel >= 1.9.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11
%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
GQmpeg is a frontend to mpg123. It includes playlist support and all
the usual playing features. Supports custom skins (looks). Uilitizes
the GTK library. Requires mpg123 v 0.59o or higher.

%description -l pl
GQmpeg jest nak³adk± graficzn± dla mpg123 - odtwarzacza plików
zapisanych w formacie MP3. Zawiera wszystkie standardowe opcje,
mo¿liwo¶æ zmiany wygl±du przy pomocy 'skórek'. GQmpeg korzysta z
biblioteki GTK i wymaga mpg123 w wersji 0.59o lub wy¿szej.

%prep
%setup -q
%patch -p0

%build
gettextize --copy --force
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	desktopdir=%{_applnkdir}/Multimedia

gzip -9nf README ChangeLog FAQ TODO SKIN-SPECS plugin/README.plugin

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz plugin/*.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_applnkdir}/Multimedia/gqmpeg.desktop
%{_datadir}/gqmpeg
%{_pixmapsdir}/*
