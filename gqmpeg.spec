Summary:	mpeg player frontend to mpg123
Summary(pl):	Nak�adka graficzna dla odtwarzacza mpg123
Name:		gqmpeg
Version:	0.12.1
Release:	2
License:	GPL
Group:		X11/Applications
Group(cs):	X11/Aplikace
Group(da):	X11/Programmer
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(fr):	X11/Applications
Group(it):	X11/Applicazioni
Group(ja):	X11/���ץꥱ�������
Group(no):	X11/Applikasjoner
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplica��es
Group(pt):	X11/Aplica��es
Group(ru):	X11/����������
Group(sv):	X11/Till�mpningar
Source0:	http://prdownloads.sourceforge.net/gqmpeg/%{name}-%{version}.tar.gz
Icon:		gqmpeg.xpm
URL:		http://gqmpeg.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
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
GQmpeg jest nak�adk� graficzn� dla mpg123 - odtwarzacza plik�w
zapisanych w formacie MP3. Zawiera wszystkie standardowe opcje,
mo�liwo�� zmiany wygl�du przy pomocy 'sk�rek'. GQmpeg korzysta z
biblioteki GTK i wymaga mpg123 w wersji 0.59o lub wy�szej.

%prep
%setup -q

%build
rm -f missing
gettextize --copy --force
aclocal
autoconf
automake -a -c
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
