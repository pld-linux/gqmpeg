Summary:	mpeg player frontend to mpg123
Summary(pl):	Nak³adka graficzna dla odtwarzacza mpg123
Name:		gqmpeg
Version:	0.6.3
Release:	1
Group:		X11/Applications/Sound
Group(pl):	X11/Aplikacje/D¼wiêk
Copyright:      GPL
Source:		http://www.geocities.com/SiliconValley/Haven/5235/%{name}-%{version}.src.tgz
Icon:		gqmpeg.xpm
Patch:		gqmpeg-desktop.patch
URL:		http://www.geocities.com/SiliconValley/Haven/5235/index.html
BuildRequires:	XFree86-devel
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	glib-devel >= 1.2.0
BuildRequires:	imlib-devel >= 1.9.4
BuildRoot:	/tmp/%{name}-%{version}-root

%define	_prefix		/usr/X11R6
%define	_sysconfdir	/etc/X11

%description
GQmpeg is a frontend to mpg123. It includes playlist support and all 
the usual playing features. Supports custom skins (looks).
Uilitizes the GTK library. Requires mpg123 v 0.59o or higher.

%description -l pl
GQmpeg jest nak³adk± graficzn± dla mpg123 - odtwarzacza plików zapisanych
w formacie MP3. Zawiera wszystkie standardowe opcje, mo¿liwo¶æ zmiany
wygl±du przy pomocy 'skórek'. GQmpeg korzysta z biblioteki GTK i wymaga
mpg123 w wersji 0.59o lub wy¿szej.

%prep
%setup -q
%patch -p0

%build
make CFLAGS="$RPM_OPT_FLAGS -I/usr/X11R6/include -I/usr/lib/glib/include"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/pixmaps} \
	$RPM_BUILD_ROOT%{_sysconfdir}/applnk/Multimedia

install -s %{name} $RPM_BUILD_ROOT%{_bindir}
install plugin/gqmpeg-shoutcast-plugin.sh $RPM_BUILD_ROOT%{_bindir}
install %{name}.png $RPM_BUILD_ROOT%{_datadir}/pixmaps
install %{name}.desktop $RPM_BUILD_ROOT%{_sysconfdir}/applnk/Multimedia

gzip -9nf README ChangeLog FAQ TODO SKIN-SPECS skindata-template \
	plugin/README.plugin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,FAQ,TODO,SKIN-SPECS,skindata-template,ChangeLog}.gz
%doc plugin/README.plugin.gz
%attr(755,root,root) %{_bindir}/*

%{_sysconfdir}/applnk/Multimedia/gqmpeg.desktop
%{_datadir}/pixmaps/gqmpeg.png
