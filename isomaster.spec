Summary:	ISO Master: graphical CD image editor
Summary(pl.UTF-8):	ISO Master - graficzny edytor obrazów płyt
Name:		isomaster
Version:	0.8.1
Release:	1
License:	GPL v2
Group:		Applications/Shells
Source0:	http://littlesvr.ca/isomaster/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	32066d9358f7f2601c3dc5344687f572
Source1:	%{name}.desktop
URL:		http://littlesvr.ca/isomaster/
BuildRequires:	gtk+2-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
Requires:	file
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
%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README.TXT CHANGELOG.TXT
%attr(755,root,root) %{_bindir}/isomaster
%dir %{_datadir}/isomaster
%dir %{_datadir}/isomaster/icons
%{_datadir}/isomaster/icons/*
%{_desktopdir}/%{name}.desktop
%{_mandir}/man1/isomaster.1*
