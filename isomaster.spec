Summary:	ISO Master: graphical CD image editor
Summary(pl):	ISO Master - graficzny edytor obrazów p³yt
Name:		isomaster
Version:	0.4
Release:	0.1
License:	GPL v2
Group:		Applications/Shells
Source0:	http://littlesvr.ca/isomaster/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	56d60c4bd37a287f936c2b9374f87c22
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

%description -l pl
ISO Master - graficzny edytor obrazów p³yt. S³u¿y do czytania,
modyfikowania i zapisywania obrazów ISO.

%prep
%setup -q
%{__sed} -i -e 's#/usr/local#/usr#;s/\<cc\>/$(CC)/' Makefile

%build
%{__make} \
	CC="%{__cc}" \
	GLOBALFLAGS="%{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.TXT CHANGELOG.TXT
%attr(755,root,root) %{_bindir}/isomaster
%dir %{_datadir}/isomaster
%dir %{_datadir}/isomaster/icons
%{_datadir}/isomaster/icons/*
%{_desktopdir}/%{name}.desktop
