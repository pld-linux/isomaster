Summary:	ISO Master: graphical CD image editor
Summary(pl.UTF-8):	ISO Master - graficzny edytor obrazów płyt
Name:		isomaster
Version:	1.3.2
Release:	1
License:	GPL v2
Group:		Applications/Shells
Source0:	http://littlesvr.ca/isomaster/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	1110ec1835f17c7a14d295fa1068131c
Source1:	%{name}.desktop
URL:		http://littlesvr.ca/isomaster/
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
Requires:	file
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ISO Master: graphical CD image editor. Used for reading, modifying and
writing ISO images.

%description -l pl.UTF-8
ISO Master - graficzny edytor obrazów płyt. Służy do czytania,
modyfikowania i zapisywania obrazów ISO.

%prep
%setup -q
%{__sed} -i -e 's#/usr/local#/usr#;s/\<cc\>/$(CC)/' Makefile

%build
%{__make} \
	CC="%{__cc}" \
	GLOBALFLAGS="%{rpmcflags} -D_FILE_OFFSET_BITS=64 -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_mandir}/man1}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/sr@Latn
%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc CHANGELOG.TXT CREDITS.TXT README.TXT
%attr(755,root,root) %{_bindir}/isomaster
%dir %{_datadir}/isomaster
%dir %{_datadir}/isomaster/icons
%{_datadir}/isomaster/icons/*
%{_desktopdir}/%{name}.desktop
%{_mandir}/man1/isomaster.1*
