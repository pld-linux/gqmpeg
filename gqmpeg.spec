Summary:	mpeg player frontend to mpg123
Summary(pl):	Nak³adka graficzna dla odtwarzacza mpg123
Name:		gqmpeg
Version:	0.91.1
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/gqmpeg/%{name}-%{version}.tar.gz
# Source0-md5:	e22eda86fc3e59108c8d04abc37b3e56
Patch0:		%{name}-desktop.patch
Icon:		gqmpeg.xpm
URL:		http://gqmpeg.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2.2.0
BuildRequires:	libpng-devel
BuildRequires:	pkgconfig
Requires:	mpg123 >= 0.59p
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GQmpeg is a frontend to mpg123. It includes playlist support and all
the usual playing features. Supports custom skins (looks). Uilitizes
the GTK+ library. Requires mpg123 v 0.59p or higher.

%description -l pl
GQmpeg jest nak³adk± graficzn± dla mpg123 - odtwarzacza plików
zapisanych w formacie MP3. Zawiera wszystkie standardowe opcje,
mo¿liwo¶æ zmiany wygl±du przy pomocy 'skórek'. GQmpeg korzysta z
biblioteki GTK+ i wymaga mpg123 w wersji 0.59p lub wy¿szej.

%prep
%setup -q
%patch0 -p1

%build
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README ChangeLog FAQ TODO SKIN-SPECS plugin/README.plugin
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_desktopdir}/gqmpeg.desktop
%{_datadir}/gqmpeg
%{_pixmapsdir}/*
