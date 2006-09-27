Summary:	A user-friendly file manager and visual shell
Summary(pl):	Midnight Commander - pow³oka wizualna
Name:		isomaster
Version:	0.4
Release:	0.1
License:	GPL2
Group:		Applications/Shells
Source0:	http://littlesvr.ca/isomaster/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	56d60c4bd37a287f936c2b9374f87c22
URL:		http://littlesvr.ca/isomaster/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	sed >= 4.0
Requires:	file
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
ISO Master: graphical CD image editor.
Used for reading, modifying and writing ISO images.

%description -l pl
ISO Master: graficzny edytor obrazów p³yt.
U¿ywany do czytania, modyfikowania i zapisywania obrazów ISO. 

%prep
%setup -q

%build
sed -i -e 's#/usr/local#/usr#' Makefile
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.TXT CHANGELOG.TXT
%attr(755,root,root) %{_bindir}/isomaster
%dir %{_datadir}/isomaster
%dir %{_datadir}/isomaster/icons
%{_datadir}/isomaster/icons/*
