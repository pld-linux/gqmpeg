Summary:	mpeg player frontend to mpg123
Summary(pl):	Nak³adka graficzna dla odtwarzacza mpg123
Name:		gqmpeg
Version:	0.5.2
Release:	2
Group:		X11/Applications/Sound
Group(pl):	X11/Aplikacje/D¼wiêk
Copyright:      GPL
URL: 		http://www.geocities.com/SiliconValley/Haven/5235/index.html
Source:		http://www.geocities.com/SiliconValley/Haven/5235/%{name}-%{version}.src.tgz
Icon:		gqmpeg.xpm
Patch:		gqmpeg-desktop.patch
BuildPrereq:	XFree86-devel
BuildPrereq:	gtk+-devel >= 1.2.0
BuildPrereq:	glib-devel >= 1.2.0
BuildPrereq:	imlib-devel >= 1.9.4
BuildRoot:	/tmp/%{name}-%{version}-root

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
make CFLAGS="$RPM_OPT_FLAGS -I/usr/X11R6/include -I%{_libdir}/glib/include"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/X11R6/{bin,share/pixmaps} \
	$RPM_BUILD_ROOT/etc/X11/applnk/Multimedia

install -s gqmpeg $RPM_BUILD_ROOT/usr/X11R6/bin
install gqmpeg.png $RPM_BUILD_ROOT/usr/X11R6/share/pixmaps
install gqmpeg.desktop $RPM_BUILD_ROOT/etc/X11/applnk/Multimedia

gzip -9nf README ChangeLog FAQ TODO SKIN-SPECS skindata-template

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,FAQ,TODO,SKIN-SPECS,skindata-template,ChangeLog}.gz
%attr(755,root,root) /usr/X11R6/bin/gqmpeg

/etc/X11/applnk/Multimedia/gqmpeg.desktop
/usr/X11R6/share/pixmaps/gqmpeg.png

%changelog
* Fri May 14 1999 Piotr Czerwiñski <pius@pld.org.pl>
  [0.5.2-2]
- spec file modified for PLD use,
- added Icon file,
- added gqmpeg-desktop.patch,
- added BuildPrereq rules,
- build on rpm 3,
- package is FHS 2.0 compliant.

* Thu May 13 1999 John Ellis <gqview@geocities.com>
- initial rpm release.
